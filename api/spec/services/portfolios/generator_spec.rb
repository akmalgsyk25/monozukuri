# frozen_string_literal: true

require 'rails_helper'

RSpec.describe Portfolios::Generator do
  let!(:org) do
    Organization.find_by(scheme: 'test-corp') || Organization.create!(
      name: 'Test Corp', scheme: 'test-corp', identifier: 'test-corp-id', host: 'localhost'
    )
  end
  let!(:user) { User.create!(email: "assessor_fe@test.com", password_digest: BCrypt::Password.create("secret123"), role: "admin") }
  let!(:assessment) do
    a = Assessment.create!(name: "Frontend Specialist", tenant_id: org.id, created_by: user.id, time_limit_min: 30)
    a.assessment_skills.create!(
      skill_id: "sk-fe-001", skill_label: "React Hooks",
      l1_anchor: "L1", l2_anchor: "L2", l3_anchor: "L3", l4_anchor: "L4", l5_anchor: "L5"
    )
    a.assessment_skills.create!(
      skill_id: "sk-fe-002", skill_label: "State Management",
      l1_anchor: "L1", l2_anchor: "L2", l3_anchor: "L3", l4_anchor: "L4", l5_anchor: "L5"
    )
    a
  end
  let!(:session) do
    s = Session.create!(assessment: assessment, tenant_id: org.id, started_at: 20.minutes.ago, status: 'active')
    s.transcript_turns.create!(turn_number: 1, speaker: 'ai', text: 'Tell me about React hooks.')
    s.transcript_turns.create!(turn_number: 2, speaker: 'candidate', text: 'I use useEffect and custom hooks for API calls.')
    s
  end

  let(:mock_gemini) { instance_double(Gemini::HttpClient) }

  context "when Gemini returns markdown-fenced JSON with unassessed skills" do
    let(:raw_gemini_response) do
      <<~JSON
        Here is the evaluation of the candidate based on the interview transcript:
        ```json
        {
          "configured_skills": [
            {
              "skill_id": "sk-fe-001",
              "skill_label": "React Hooks",
              "level": 3,
              "confidence": "high",
              "evidence": ["I use useEffect and custom hooks for API calls."],
              "competency_summary": "Demonstrates solid understanding of hook lifecycle."
            },
            {
              "skill_id": "sk-fe-002",
              "skill_label": "State Management",
              "level": null,
              "confidence": "low",
              "evidence": [],
              "competency_summary": "Skill was not explored in the interview."
            }
          ],
          "discovered_skills": [
            {
              "skill_label": "API Optimization",
              "level": 2,
              "confidence": "medium",
              "evidence": ["Custom hooks for API calls."],
              "competency_summary": "Understands request encapsulation."
            }
          ]
        }
        ```
        Let me know if you need anything else!
      JSON
    end

    before do
      allow(mock_gemini).to receive(:generate_content).and_return(raw_gemini_response)
    end

    it "successfully parses markdown-fenced JSON and preserves nil for unassessed skills" do
      generator = described_class.new(session: session, gemini_client: mock_gemini)
      portfolio = generator.call

      expect(portfolio.generation_status).to eq('complete')
      expect(portfolio.portfolio_skills.count).to eq(3)

      react_skill = portfolio.portfolio_skills.find_by(skill_id: "sk-fe-001")
      expect(react_skill.ai_level).to eq(3)
      expect(react_skill.ai_confidence).to eq("high")
      expect(react_skill.evidence_quotes).to include("I use useEffect and custom hooks for API calls.")

      unassessed_skill = portfolio.portfolio_skills.find_by(skill_id: "sk-fe-002")
      expect(unassessed_skill.ai_level).to be_nil
      expect(unassessed_skill.ai_confidence).to eq("low")

      discovered_skill = portfolio.portfolio_skills.find_by(is_discovered: true)
      expect(discovered_skill.skill_label).to eq("API Optimization")
      expect(discovered_skill.ai_level).to eq(2)
    end
  end

  context "when Gemini call raises an error" do
    before do
      allow(mock_gemini).to receive(:generate_content).and_raise(StandardError.new("API rate limit exceeded"))
    end

    it "marks portfolio generation_status as failed with error details" do
      generator = described_class.new(session: session, gemini_client: mock_gemini)

      expect { generator.call }.to raise_error(StandardError, "API rate limit exceeded")

      portfolio = session.reload.portfolio
      expect(portfolio.generation_status).to eq('failed')
      expect(portfolio.generation_error).to eq("API rate limit exceeded")
    end
  end
end
