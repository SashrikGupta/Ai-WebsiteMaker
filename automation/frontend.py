



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

    index_js_content =  """
      
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

    
  """


    html_content = """
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

"""



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




    