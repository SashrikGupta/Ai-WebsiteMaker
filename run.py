import os
import subprocess
import sys


def create_virtual_env(env_name='venv'):
    subprocess.check_call([sys.executable, '-m', 'venv', env_name])
    print(f"Created virtual environment: {env_name}")

def install_packages(env_name='venv'):
    if os.name == 'nt':
        pip_path = os.path.join(env_name, 'Scripts', 'pip')
    else:
        pip_path = os.path.join(env_name, 'bin', 'pip')
    
    subprocess.check_call([pip_path, 'install', 'flask', 'flask-cors', 'psutil'])
    print("Installed Flask, Flask-CORS, and psutil")

def activate_virtual_env_and_run(env_name='venv', script_name='run_in_venv.py'):
    if os.name == 'nt':
        python_path = os.path.join(env_name, 'Scripts', 'python')
    else:
        python_path = os.path.join(env_name, 'bin', 'python')
    
    subprocess.check_call([python_path, script_name])
    print(f"Ran script {script_name} within virtual environment {env_name}")


env_name = 'venv'

script_content = """


import os
import subprocess
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
import psutil

app = Flask(__name__)
servers = []
CORS(app)



# area for execution bedore the code runnig 


def stop_server_on_port(port):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.name() == 'node' and f':2004' in ' '.join(proc.cmdline()):  # Checking if 'node' and port in cmdline
                print(f"Found Node.js process on port 2004 , terminating...")
                proc.terminate()
                print("Process terminated.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass






if not os.path.exists("react_server"):


  init_command = "npm init vite@latest react_server -- --template react"
  init_result = subprocess.run(init_command, shell=True, check=True, capture_output=True, text=True)
  print(init_result.stdout)
  print(init_result.stderr)

  os.chdir("react_server/src")

  intial_frontend = \"\"\"

import { useState } from 'react';
import './App.css';

function App() {
  const [reloadKey, setReloadKey] = useState(0);
  const [idea, setIdea] = useState('');
  const [frontendSuggestion, setFrontendSuggestion] = useState('');
  const [additionalChanges, setAdditionalChanges] = useState('');

  const handleAdditionalSubmit = async () => {
    try {
      const response = await fetch("http://localhost:4000/change_frontend", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: additionalChanges
        })
      });

      const data = await response.json();
      console.log(data); // Check the response data

      await fetch("http://localhost:5000/make_change", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });
    } catch (error) {
      console.error('Error submitting additional changes:', error);
    }
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch("http://localhost:4000/code", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: idea,
          front: frontendSuggestion
        })
      });

      const data = await response.json();
      console.log(data); // Check the response data

      await fetch("http://localhost:5000/make_change", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });
    } catch (error) {
      console.error('Error submitting idea:', error);
    }
  };

  return (
    <div className='w-screen h-screen flex justify-center items-center'>
      <div className='flex w-[90vw] h-[60vh] justify-around items-center flex-wrap'>
        <iframe
          key={reloadKey}
          src="http://localhost:5173"
          title="Embedded Website"
          className='h-[50vh] w-[50vw] rounded-lg shadow-xl'
        />
        <div className='w-[30vw] h-[50vh] flex flex-col justify-around'>
          <div className='flex flex-col justify-center items-center w-[30vw] h-[30vh] bg-[#333333] rounded-lg shadow-xl p-4'>
            <h1 className='text-2xl font-bold mb-4'>
              Convert your ideas to full stack website
            </h1>
              <button
                onClick={() => window.location.href = 'http://localhost:5173/'}
                className='w-full mb-4 p-2 bg-blue-500 text-white rounded'
              >
                Go to your website
              </button>
            <input
              type="text"
              placeholder="Your Idea"
              value={idea}
              onChange={(e) => setIdea(e.target.value)}
              className='w-full p-2 mb-4 rounded'
            />
            <input
              type="text"
              placeholder="Frontend Suggestion"
              value={frontendSuggestion}
              onChange={(e) => setFrontendSuggestion(e.target.value)}
              className='w-full p-2 mb-4 rounded'
            />
            <button
              onClick={handleSubmit}
              className='w-full p-2 bg-red-500 text-white rounded'
            >
              Submit
            </button>
          </div>
          <div className='flex flex-col justify-center items-center w-[30vw] h-[14vh] bg-[#333333] rounded-lg shadow-xl p-4'>
            <input
              type="text"
              placeholder="Additional Frontend Changes"
              value={additionalChanges}
              onChange={(e) => setAdditionalChanges(e.target.value)}
              className='w-full p-2 mb-2 rounded'
            />
            <button
              onClick={handleAdditionalSubmit}
              className='w-full p-2 bg-red-500 text-white rounded'
            >
              Submit Changes
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

\"\"\"
  html_content = \"\"\"
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
\"\"\"
  css_content = \"\"\"


.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.react:hover {
  filter: drop-shadow(0 0 2em #61dafbaa);
}

@keyframes logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: no-preference) {
  a:nth-of-type(2) .logo {
    animation: logo-spin infinite 20s linear;
  }
}

.card {
  padding: 2em;
}

.read-the-docs {
  color: #888;
}


\"\"\"
  vite_content = \"\"\"

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: 9000
  },
  plugins: [react()],
})


\"\"\"

  with open('App.jsx', 'w') as file:  # Write to App.jsx
      file.write(intial_frontend)
  with open('App.css', 'w') as file:  # Write to App.jsx
      file.write(css_content)
  os.chdir("..")
  with open('index.html', 'w') as file:  # Write to App.jsx
      file.write(html_content)
  with open("vite.config.js" , 'w') as file : 
      file.write(vite_content)
  install_result = subprocess.run("npm install", shell=True, check=True, capture_output=True, text=True)
  print(install_result.stdout)
  print(install_result.stderr)
  os.chdir("..")

if not os.path.exists("Js_server"):
    os.mkdir("Js_server")
    os.chdir("Js_server")
    init_result = subprocess.run("npm init -y", shell=True, check=True)
    print(init_result.stdout)
    print(init_result.stderr)

    # Step 2: Install dependencies
    install_result = subprocess.run("npm install express cors morgan mongoose @google/generative-ai", shell=True, check=True)
    print(install_result.stdout)
    print(install_result.stderr)

    intial_backend = \"\"\"

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
       give nodejs and react js code to the following : 
         ${text}
      note  : in any code do not provide documentations only code just code
      note : use same port for both which is 2004
      note for backend :with local mongodb and cors 
      note for tailwind : achieve ${front} by using tailwind and inline css only 
      note for frontend : use http://localhost:2004/ as base url  , for frontend and write code for App.jsx
      using the JSON schema:
       {
           "backend": { "type": "string" }
           "frontend": {"type" : "string" }
      }`;
       
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

\"\"\"

    with open('index.js', 'w') as file:  # Write to App.jsx
        file.write(intial_backend)
    os.chdir("..")

backend_text =\"\"\"
  // backend/index.js
  const express = require('express');
  const cors = require('cors');
  const morgan = require('morgan');
  require("dotenv").config();

  const app = express();

  const PORT = process.env.PORT || 3000;
  app.use(express.json());
  app.use(cors());
  app.use(express.urlencoded({ extended: true }));
  app.use(morgan('dev'));

  app.get("/random", (req, res) => {
      const randomNumber = Math.floor(Math.random() * 100);
      res.json({ number: randomNumber });
  });

  app.listen(PORT, () => {
      console.log("server has been started at link: " + `http://localhost:${PORT}/`);
  });
    \"\"\"
frontend_text = \"\"\"
    // frontend/src/App.jsx
    import React, { useState, useEffect } from 'react';
    import reactLogo from './assets/react.svg';
    import viteLogo from '/vite.svg';
    import './App.css';

    function App() {
      const [number, setNumber] = useState(null);

      const fetchNumber = async () => {
        try {
          const response = await fetch("http://localhost:3000/random");
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          const data = await response.json();
          setNumber(data.number);
        } catch (error) {
          console.error('Error fetching number:', error);
        }
      };

      useEffect(() => {
        fetchNumber();
      }, []);

      return (
        <>
          <div>
            <a href="https://vitejs.dev" target="_blank" rel="noopener noreferrer">
              <img src={viteLogo} className="logo" alt="Vite logo" />
            </a>
            <a href="https://react.dev" target="_blank" rel="noopener noreferrer">
              <img src={reactLogo} className="logo react" alt="React logo" />
            </a>
          </div>
          <h1>Vite + React</h1>
          <div className="card">
            <button onClick={fetchNumber}>
              Get Random Number
            </button>
            {number !== null && <p>Random number is {number}</p>}
            <p>
              Edit <code>src/App.jsx</code> and save to test HMR
            </p>
          </div>
          <p className="read-the-docs">
            Click on the Vite and React logos to learn more
          </p>
        </>
      );
    }

    export default App;

    \"\"\"
directories = ["project", "automation"]
# Check and create directories if they don't exist
for directory in directories:
      if not os.path.exists(directory):
          os.mkdir(directory)
          print(f"Directory '{directory}' created.")
      else:
          print(f"Directory '{directory}' already exists.")


os.chdir("automation")
with open('backend.py', 'w') as file:  # Write to App.jsx
      file.write(f\"\"\"

import os
import subprocess

# Define the project path
project_path = 'project/server'

try:
    # Create the directory if it does not exist
    os.makedirs(project_path, exist_ok=True)
    os.chdir(project_path)

    # Step 1: Initialize a new Node.js project
    init_result = subprocess.run("npm init -y", shell=True, check=True)
    print(init_result.stdout)
    print(init_result.stderr)

    # Step 2: Install dependencies
    install_result = subprocess.run("npm install express cors morgan mongoose", shell=True, check=True)
    print(install_result.stdout)
    print(install_result.stderr)
    
except subprocess.CalledProcessError as e:
    # Print the error if any subprocess command fails
    print("An error occurred while running npm commands:")
except Exception as e:
    # Handle other exceptions
    print("An unexpected error occurred: ")

# Define the content of index.js
index_js_content =  \\"\\"\\"
{backend_text}
\\"\\"\\"

try:
    # Write the content to index.js
    with open('index.js', 'w') as file:
        file.write(index_js_content)
    print("index.js has been created successfully.")
    subprocess.run("mkdir models" , shell=True, check=True)
    print("models created ")
    subprocess.run("mkdir controllers" , shell=True, check=True)
    print("controllers created ")
    subprocess.run("mkdir routes" , shell=True, check=True)
    print("routes created ")
    print("mvc model intialized")
except Exception as e:
    print("An error occurred while writing to index.js:")

try:
    # Start the server with nodemon
    nodemon_result = subprocess.run("node index.js", shell=True, check=True)
    print(nodemon_result.stdout)
    print(nodemon_result.stderr)
    print("nodemon intialized")
except subprocess.CalledProcessError as e:
    # Print the error if any subprocess command fails
    print("An error occurred while starting nodemon:")
except Exception as e:
    # Handle other exceptions
    print("An unexpected error occurred:")

    \"\"\")
with open('frontend.py', 'w') as file:  # Write to App.jsx
      file.write(f\"\"\"



import os
import subprocess

# Define absolute paths for project structure
project_path = os.path.abspath("project")
client_src_path = os.path.join(project_path, "client", "src")

try:
    # Create the directory if it does not exist
    os.makedirs(project_path, exist_ok=True)
    os.chdir(project_path)

    # Step 1: Initialize a new vite project non-interactively
    init_command = "npm init vite@latest client -- --template react"
    init_result = subprocess.run(init_command, shell=True, check=True, capture_output=True, text=True)
    
    print(init_result.stdout)
    print(init_result.stderr)

    index_js_content =  \\"\\"\\"
      {frontend_text}
  \\"\\"\\"


    html_content = \\"\\"\\"
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>

\\"\\"\\"



    os.makedirs(client_src_path, exist_ok=True)  # Create client/src directory if not exists
    os.chdir(client_src_path)  # Change directory to client/src
    with open('App.jsx', 'w') as file:  # Write to App.jsx
        file.write(index_js_content)
    print("App.jsx has been changed successfully.")

    os.chdir(os.path.join(project_path, "client"))  # Adjust path for npm commands
    with open('index.html', 'w') as file:  # Write to App.jsx
        file.write(html_content)
    # Step 2: Install dependencies
    install_result = subprocess.run("npm install", shell=True, check=True, capture_output=True, text=True)
    print(install_result.stdout)
    print(install_result.stderr)
    install_result = subprocess.run("npm install axios chart.js react-chartjs-2 ", shell=True, check=True, capture_output=True, text=True)
    print(install_result.stdout)
    print(install_result.stderr)
    # Step 3: Start the project
    start_result = subprocess.run("npm run dev", shell=True, check=True, capture_output=True, text=True)
    print(start_result.stdout)
    print(start_result.stderr)

except subprocess.CalledProcessError as e:
    print("An error occurred while running npm commands: ")
except Exception as e:
    print("An unexpected error occurred: ")




    \"\"\")
os.chdir("..")

def start_server(file_name):
   return subprocess.Popen(["python", file_name])

def stop_server(process):
    process.terminate()
def start_servers():
    print(os.getcwd())
    os.chdir("react_server")
    actual_frontend = subprocess.Popen(["npm", "run", "dev"] ,  shell=True)
    os.chdir("..")
    os.chdir("Js_server")
    actual_backend = subprocess.Popen(["node" , "index.js"], shell=True)
    os.chdir("..")
    # Start backend server
    backend_process = start_server("automation/backend.py")
    print("Backend server started.")

    # Start frontend server
    frontend_process = start_server("automation/frontend.py")
    print("Frontend server started.")

    return [backend_process , frontend_process , actual_frontend , actual_backend]




servers = start_servers()





# Mock functions to simulate server operations




def change(backend, frontend):
    # Implement make change functionality
    stop_server_on_port(2004)
    with open('change.py', 'w') as file:
      file.write(f\"\"\"
import os
import subprocess
def change_backend(index_js_content):
    os.chdir("project/server")
    with open('index.js', 'w') as file:
        file.write(index_js_content)
    subprocess.Popen(["node" , "index.js"], shell=True)
    os.chdir("../..")

def change_frontend(index_js_content):
    print(os.getcwd())
    os.chdir("project/client/src")
    with open('App.jsx', 'w') as file:
        file.write(index_js_content)
    with open('App.css', 'w') as file:
        file.write(" ")
    with open('index.css', 'w') as file:
        file.write(" ")
    os.chdir("../../..")

def change_backend_and_frontend(back, front):
    change_backend(back)
    change_frontend(front)

change_backend_and_frontend(\\"\\"\\"{backend}\\"\\"\\", \\"\\"\\"{frontend}\\"\\"\\")
\"\"\")
    
    start_server("change.py")
    return f"{frontend}"


# Routes



@app.route('/make_change', methods=['POST'])
def make_change_route():
    data = request.get_json()
    print(data)
    backend = data.get('backend')
    frontend = data.get('frontend')
    print(backend)
    print(frontend)
    result = change(backend, frontend)
    return result


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)






""" 


if not os.path.exists(env_name):
    create_virtual_env(env_name)
    install_packages(env_name)
    with open("run_in_venv.py", "w") as script_file:
      script_file.write(script_content)
else:
    print(f"Virtual environment '{env_name}' already exists.")

# Create a script to run within the virtual environment
# Run the script within the virtual environment
activate_virtual_env_and_run(env_name, 'run_in_venv.py')
