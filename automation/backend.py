

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
    install_result = subprocess.run("npm install express cors morgan mongoose @google/generative-ai", shell=True, check=True)
    print(install_result.stdout)
    print(install_result.stderr)
    
except subprocess.CalledProcessError as e:
    # Print the error if any subprocess command fails
    print("An error occurred while running npm commands:")
except Exception as e:
    # Handle other exceptions
    print("An unexpected error occurred: ")

# Define the content of index.js
index_js_content =  """

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
    
"""

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
    nodemon_result = subprocess.run("nodemon start", shell=True, check=True)
    print(nodemon_result.stdout)
    print(nodemon_result.stderr)
    print("nodemon intialized")
except subprocess.CalledProcessError as e:
    # Print the error if any subprocess command fails
    print("An error occurred while starting nodemon:")
except Exception as e:
    # Handle other exceptions
    print("An unexpected error occurred:")

    