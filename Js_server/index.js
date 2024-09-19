

const { GoogleGenerativeAI } = require("@google/generative-ai");
const express = require("express")
const cors = require('cors')

const app = express();
const port = process.env.PORT || 4000;
app.use(cors());
app.use(express.json());
// setting up dotenv
require('dotenv').config()

console.log(process.env.API_KEY)
// Access your API key as an environment variable (see "Set up your API key" above)
const genAI = new GoogleGenerativeAI("AIzaSyC2w_s0gzTC5bNkDeiOnloUdKf7RAIIlbM");
let model_backend = genAI.getGenerativeModel({
   model: "gemini-1.5-flash",
   // Set the `responseMimeType` to output JSON
   generationConfig: { responseMimeType: "application/json" }
 });

 const genAI2 = new GoogleGenerativeAI("AIzaSyDMGiZds8QE2MquY0tm7N4qE4_zBUXOKM8");
let model_frontend = genAI2.getGenerativeModel({
   model: "gemini-1.5-flash",
   // Set the `responseMimeType` to output JSON
   generationConfig: { responseMimeType: "application/json" }
 });
 let data 
// Using `responseMimeType` requires one of the Gemini 1.5 Pro or 1.5 Flash models
const run = async(text , front)=>{
   try {


       let prompt = `
       give nodejs and react js codes to the following : 
         ${text}
      note  : in any code do not provide documentations only code just code
      note : use same port for both which is 2004
      note for backend :with local mongodb and cors 
      note for backend : make models of database in the same file only 
      note for backend : to import modules only use require function
      note for tailwind : achieve ${front} and card effect , shadow effect  , hover transitions with 
                           backgound linear gradient from aqua to puple to pink 
                         from by using tailwind and inline css only 
      note : you have to use api as demonstrated below 

      use this google llm to generate additional content that has been asked : 
        for thet you can refer the below code to add in your code : 

            const { GoogleGenerativeAI } = require("@google/generative-ai");
            const genAI = new GoogleGenerativeAI("AIzaSyC2w_s0gzTC5bNkDeiOnloUdKf7RAIIlbM");
            const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

                        async function run() {
            const prompt = "Write a story about a AI and magic"

            const result = await model.generateContent(prompt);
            const response = await result.response;
            const text = response.text();
            console.log(text);
            }
            run()

      note : in order to generate url of images use the below function that can give images based on image title 
            "
               async function give_image_by_title(title)
         {
            title = title.replace(/ /g, '+') ;
            const response =  await fetch(\`https://api.unsplash.com/search/photos?page=1&query=\${title}&client_id=J3Af0qhs3oT2DAqbTjP9IAwgM575BYNOrJlAcC-BtZs\`)
            const data = await response.json()
            return data.results[0].urls.raw
         }

         const data = await give_image_by_title("night city")
         the result will be url to the image and title passed to function should be small 
                          
      note for frontend : use http://localhost:2004/ as base url  , for frontend and write code for App.jsx
      using the JSON schema:
       {
           "backend": { "type": "string" }
           "frontend": {"type" : "string" }
      }`;

      console.log(prompt)
       
       let result = await model_backend.generateContent(prompt)
       console.log(JSON.parse(result.response.text()).frontend)
       console.log(JSON.parse(result.response.text()).backend)
       return JSON.parse(result.response.text())
   }
   catch(error){
      console.log(error) ;
   }

}


app.post("/code" , async(req , res)=>{
   const {text , front} = req.body
   data = await run(text , front)
   res.status(200).json(data) ;
})

app.post("/change_frontend"  , async(req , res)=>{
   const {text} = req.body
   let prompt = `
   change the following code :
    ${data.frontend}
   for the following feature :
   ${text} 
  only using tailwind css 
  provide the entire code : 
  using the JSON schema:
   {
       "frontend": {"type" : "string" }
  }`;
   
   let result = await model_frontend.generateContent(prompt)
   new_frontend = JSON.parse(result.response.text()).frontend
   data.frontend = new_frontend
   res.status(200).json({backaend : data.backend , frontend : new_frontend})
})

app.listen(port, () => {
   console.log(`Server listening on port ${port}`);
 });



