const { GoogleGenerativeAI } = require("@google/generative-ai");
const genAI = new GoogleGenerativeAI("AIzaSyC2w_s0gzTC5bNkDeiOnloUdKf7RAIIlbM");
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

            async function run() {
const prompt = "Write a react code that uses appwrite that use RAG model to read pdf using langchain"

const result = await model.generateContent(prompt);
const response = await result.response;
const text = response.text();
console.log(text);
}
run()