# AI Research Assistant: Frontend (Next.js)

Made completely with Windsurf AI

---

## 📚 Project Overview

This is the frontend component of the AI Research Assistant application, built with Next.js using TypeScript and Tailwind CSS. It provides an interactive chat interface for users to interact with the AI assistant and manage research documents. It lives in a monorepo alongside a FastAPI backend, ensuring seamless integration.

---

## ✨ Features

- Scalable Component Structure  
  - Organized into `src/components/ui`, `src/components/layout`, and `src/features/chat` for reusable UI elements and feature-specific code.  
  - Key components:  
    - **Button.tsx**: A reusable UI button with customizable styles.  
    - **ChatWindow.tsx**: Main chat interface, managing conversation state and layout.  
    - **MessageList.tsx**: Displays conversation history with auto-scrolling.  
    - **ChatInput.tsx**: User input area with send button and keyboard submission support.  

- Zustand for State Management  
  Utilizes a lightweight store (`src/stores/chatStore.ts`) to manage chat state, including the messages array, threadId, loading status, and real-time update actions.

- Client Components  
  Marks interactive pieces (ChatWindow, MessageList, ChatInput) as Client Components to ensure correct React behavior under Next.js’s App Router.

- Streaming API Client  
  - `src/lib/api.ts` exports an asynchronous `sendChatMessage` function.  
  - Sends POST requests to the FastAPI backend, handles streaming responses via `ReadableStream` and `TextDecoder`, and updates the Zustand store token by token.

- Dynamic Backend Connectivity  
  Reads the backend URL from the `NEXT_PUBLIC_API_URL` environment variable for flexible deployment and local development.

---

## 🛠️ Technologies Used

- Next.js 14.2.3 (App Router)  
- React  
- TypeScript  
- Tailwind CSS  
- Zustand (state management)  
- pnpm (monorepo and package management)

---

## ⚙️ Setup and Installation (Local Development)

1. Clone the monorepo  
   ```bash
   git clone <your-repo-url>
   ```
2. Navigate to the frontend directory  
   ```bash
   cd apps/web
   ```
3. Create a `.env.local` file and set your backend URL  
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```
4. Install dependencies  
   ```bash
   pnpm install
   ```
5. Run the development server  
   ```bash
   pnpm dev
   ```
6. Open your browser at the URL shown in the terminal (e.g., `http://localhost:3000`).

---

## 🚀 Deployment

The frontend is deployed on Vercel.  
Frontend URL: https://ainextfastapi-ddsm2j1iz-imcoder2018s-projects.vercel.app/

---

## Acknowledgements

This project was made completely with Windsurf AI, showcasing its strengths in full-stack development—from project scaffolding and environment setup to frontend/backend integration, testing, and Dockerization.
