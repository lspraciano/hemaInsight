# Hemato Insight

This project has two goals: to demonstrate the possibility of applying
artificial intelligence in healthcare and to show how we can use a YOLO
model as a tool for an LLM model. Through natural language and via the
terminal, users can have a conversation with the agent. This agent has
three tools: one for detections using a YOLOv10 model trained to detect
leukocytes, another to list images in a specific folder, and the last
one to display images on the screen for the user.

This project leverages the powerful YOLO models provided by the
[Ultralitycs](https://docs.ultralytics.com/pt/models/yolov10/)library
for object detection and combines it with advanced natural language
processing using [LangChain](https://www.langchain.com/) and
[LangGraph](https://www.langchain.com/langgraph) to enable seamless interaction
between the user and the AI agent.

![compiled_graph.png](compiled_graph.png)

## 🗂️ Table of Contents

- [☑️ Project Status](#-project-status)
- [☄️ Current Version](#-current-version)
- [📁️ Project Structure](#-project-structure)
    - [📂database](#database)
    - [📂images](#images)
    - [📂machine_learning](#machine_learning)
- [📋 main.py File](#-mainpy-file)
- [🌠 Cloning the Project](#-cloning-the-project)
- [✈️ Installation](#-installation)
- [🔧 Configuration](#-configuration)
    - [Creating ".env"](#creating-env)
- [🚀 Running the Application](#-running-the-application)
- [🔭 Usage Example](#-usage-example)
    - [Vídeo Exemple](#vídeo-exemple)
    - [Text Exemple](#text-exemple)
- [⚠️ Notes](#-notes)

## ☑️ Project Status

- In Development

### ☄️ Current Version

- 0.1.0

## 📁️ Project Structure

### 📂database

Folder designated to hold SQLite database connection files, which will
be used for memory persistence.

### 📂images

This folder is intended to store the input and output images of this
project. It contains two subfolders:

1. detections
2. originals

The `detections` folder is used to store the predictions made by the
YOLO model, while the `originals` folder is used to store the original
images that the agent will analyze to make its inferences.

### 📂machine_learning

This folder contains the core of the application. It is divided into
two subfolders:

1. cnn
2. llm

In the `cnn` folder, you'll find the code that supports functionalities
involving image detection. For example, the trained leukocyte
detection model will be located in `cnn_models`. In the `llm`
folder, you'll find the entire graph structure. The graph is divided
into its main components, such as Edges, Nodes, etc.

### 📋 main.py File

This is the main file and includes the following functionalities:

- **`main()`**:
    - A loop that captures user input.
    - Processes messages using the `compiled_graph`.
    - Displays the generated response in the console.

## 🌠 Cloning the Project

### Cloning the Main Repository

To clone the project, use the following command.

```bash
git clone https://github.com/lspraciano/hemaInsight.git
```

## ✈️ Installation

Once the project is cloned and you are in the root directory,
you can install the dependencies.

### Installing

```bash
poetry install
poetry shell
```

## 🔧 Configuration

Before running the project, some configuration is needed. Create a
`.env` file in the project's root directory.

### Creating ".env"

On Windows:

```bash
echo. > .env
```

On Linux:

```bash
touch .env
```

In this file, provide your OpenAI key:

```
OPENAI_API_KEY=...
```

## 🚀 Running the Application

To run the application, use the following command:

```bash
python main.py
```

## 🔭 Usage Example

### Vídeo Exemple

[![Leukocyte Detection Video](https://img.youtube.com/vi/0D92Rvi_4JA/0.jpg)](https://youtu.be/0D92Rvi_4JA)

### Text Exemple

```
- User: Hello
- Agent: Hello! How can I assist you today?

- User: What cells have been identified?
- Agent: To identify the cells, I need access to the images where they are located.
          Please provide the path to the folder containing the images for analysis.

- User: The path to the images is ./images/originals
- Agent: Here are the cells identified in the provided images:

1. **Image 1**:
   - Lymphocyte
   - Lymphocyte

...

```

### ⚠️ Notes

- The default path where you should place the images is `./images/originals`.
- The agent can provide additional information, such as cell areas, types,
- and suggestions for cells requiring review, and even display the
- images on your screen.

