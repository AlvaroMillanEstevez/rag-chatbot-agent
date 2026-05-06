<template>
  <main class="app">
    <section class="hero">
      <nav class="navbar">
        <div class="brand">
          <div class="brand-icon">AI</div>
          <span>RAG Chatbot Agent</span>
        </div>

        <a
          href="https://github.com/AlvaroMillanEstevez/rag-chatbot-agent"
          target="_blank"
          rel="noopener noreferrer"
          class="github-link"
        >
          GitHub
        </a>
      </nav>

      <div class="hero-grid">
        <div class="hero-content">
          <p class="eyebrow">FastAPI · LlamaIndex · Ollama · Chroma · Vue</p>

          <h1>AI Website Assistant trained on your documents</h1>

          <p class="hero-description">
            A local RAG chatbot that answers questions using a custom knowledge
            base, retrieves relevant context and shows the sources used to
            generate each answer.
          </p>

          <div class="hero-actions">
            <button class="primary-button" @click="focusChatInput">
              Try the chatbot
            </button>

            <div class="example-questions">
              <p>Try asking:</p>

              <div class="example-list">
                <button
                  v-for="example in exampleQuestions"
                  :key="example"
                  type="button"
                  @click="askExampleQuestion(example)"
                >
                  {{ example }}
                </button>
              </div>
            </div>
          </div>

          <div class="features">
            <article>
              <span>01</span>
              <strong>Document ingestion</strong>
              <p>
                Loads Markdown, TXT, PDF and DOCX files into a vector database.
              </p>
            </article>

            <article>
              <span>02</span>
              <strong>Local AI model</strong>
              <p>
                Uses Ollama locally, avoiding external AI API keys for the demo.
              </p>
            </article>

            <article>
              <span>03</span>
              <strong>Source citations</strong>
              <p>
                Shows which document chunks were used to generate each answer.
              </p>
            </article>
          </div>
        </div>

        <section class="chat-card" aria-label="AI chatbot demo">
          <div class="chat-header">
            <div>
              <p class="chat-label">Live Demo</p>
              <h2>Website AI Assistant</h2>
            </div>

            <div class="chat-header-actions">
              <div class="status">
                <span class="status-dot"></span>
                Local RAG
              </div>

              <button type="button" class="clear-button" @click="clearChat">
                Clear
              </button>
            </div>
          </div>

          <div ref="messagesContainer" class="messages">
            <div class="message assistant">
              <div class="avatar">AI</div>
              <div class="bubble">
                <p>
                  Hi! Ask me something about the demo application documentation.
                  For example: <strong>How can I archive an user?</strong>
                </p>
              </div>
            </div>

            <div
              v-for="message in messages"
              :key="message.id"
              class="message"
              :class="message.role"
            >
              <div class="avatar">
                {{ message.role === "user" ? "You" : "AI" }}
              </div>

              <div class="bubble">
                <p>{{ message.content }}</p>

                <div
                  v-if="message.sources && message.sources.length"
                  class="sources"
                >
                  <button
                    type="button"
                    class="sources-toggle"
                    @click="message.showSources = !message.showSources"
                  >
                    {{ message.showSources ? "Hide sources" : "Show sources" }}
                    <span>{{ message.sources.length }}</span>
                  </button>

                  <div v-if="message.showSources" class="source-list">
                    <article
                      v-for="(source, index) in message.sources"
                      :key="`${source.file_name}-${index}`"
                      class="source-item"
                    >
                      <div class="source-meta">
                        <strong>{{
                          source.file_name || "Unknown document"
                        }}</strong>
                        <span v-if="source.score">
                          Score: {{ Number(source.score).toFixed(3) }}
                        </span>
                      </div>

                      <p>{{ source.text }}</p>
                    </article>
                  </div>
                </div>
              </div>
            </div>

            <div v-if="isLoading" class="message assistant">
              <div class="avatar">AI</div>
              <div class="bubble loading-bubble">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>

          <form class="chat-form" @submit.prevent="sendMessage">
            <textarea
              ref="chatInput"
              v-model="question"
              rows="2"
              placeholder="Ask something about the documentation..."
              @keydown.enter.exact.prevent="sendMessage"
            ></textarea>

            <button type="submit" :disabled="isLoading || !question.trim()">
              {{ isLoading ? "Thinking..." : "Send" }}
            </button>
          </form>

          <p v-if="errorMessage" class="error-message">
            {{ errorMessage }}
          </p>
        </section>
      </div>
    </section>
  </main>
</template>

<script setup>
import { nextTick, ref } from "vue";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

const question = ref("");
const messages = ref([]);
const isLoading = ref(false);
const errorMessage = ref("");
const chatInput = ref(null);
const messagesContainer = ref(null);

const focusChatInput = () => {
  chatInput.value?.focus();
};

const exampleQuestions = [
  "How can I archive an user?",
  "What happens to archived users?",
  "Who can change order status?",
  "What information is stored in a support ticket?",
  "What should the chatbot do if it does not have enough information?",
];

const askExampleQuestion = (example) => {
  question.value = example;
  focusChatInput();
};

const scrollToBottom = async () => {
  await nextTick();

  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
  }
};

const sendMessage = async () => {
  const cleanQuestion = question.value.trim();

  if (!cleanQuestion || isLoading.value) {
    return;
  }

  errorMessage.value = "";

  messages.value.push({
    id: crypto.randomUUID(),
    role: "user",
    content: cleanQuestion,
  });

  question.value = "";
  isLoading.value = true;

  await scrollToBottom();

  try {
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        question: cleanQuestion,
      }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(errorText || "The API returned an error.");
    }

    const data = await response.json();

    messages.value.push({
      id: crypto.randomUUID(),
      role: "assistant",
      content: data.answer,
      sources: data.sources || [],
      showSources: true,
    });
  } catch (error) {
    console.error(error);

    errorMessage.value =
      "Could not connect to the chatbot API. Make sure FastAPI is running on port 8000.";

    messages.value.push({
      id: crypto.randomUUID(),
      role: "assistant",
      content:
        "Sorry, I could not generate an answer right now. Please check that the backend and Ollama are running.",
    });
  } finally {
    isLoading.value = false;
    await scrollToBottom();
  }
};

const clearChat = () => {
  messages.value = [];
  errorMessage.value = "";
  question.value = "";
  focusChatInput();
};
</script>
