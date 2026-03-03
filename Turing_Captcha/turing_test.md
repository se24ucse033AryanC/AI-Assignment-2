# Turing Test Implementation

## Objective
The Turing Test checks whether a machine can imitate human conversation.

If a human judge cannot correctly identify which participant is the machine, the machine passes the test.

---

## Architecture

Participants:
- Human Judge
- Human Participant
- AI Chatbot

System Components:
1. Chat Interface
2. Message Router
3. AI Model
4. Human Response Channel
5. Evaluation Module

---

## Working Process

1. Judge sends a message.
2. System forwards message to both human and AI.
3. Both send replies.
4. Judge evaluates responses.
5. Judge decides which is machine.

---

## Agent Perspective

AI chatbot acts as:
- Goal-Based Agent (goal: appear human)
- Uses NLP model
- Generates human-like responses