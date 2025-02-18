## **📌 Personalized Chatbot**

🚀 A **streamlit-based chatbot** using **Cohere AI** to generate responses in real-time.

## Live - https://pchatbot.streamlit.app/

---

## **📋 Features**

✅ **Real-time AI-generated responses** using Cohere API\
✅ **Interactive Streamlit UI** for seamless chat experience\
✅ **Efficient backend processing** with Cohere's `command-r-plus` model\
✅ **Supports streaming responses** for a dynamic chat experience

---

## **🛠️ Tech Stack**

🔹 **Frontend:** Streamlit\
🔹 **Backend:** Python, Cohere API\
🔹 **Environment Management:** dotenv

---

## **🚀 Installation & Setup**

### **1️⃣ Clone the Repository**

```sh
git clone https://github.com/your-username/personalized-chatbot.git
cd personalized-chatbot
```

### **2️⃣ Create a Virtual Environment (Recommended)**

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

*(Ensure **`requirements.txt`** is generated using **`pip freeze > requirements.txt`** before pushing to GitHub.)*

### **4️⃣ Set Up Environment Variables**

- **Create a **``** file** in the project directory
- Add your Cohere API Key:
  ```
  COHERE_API_KEY="**your-api-key-here**"  
  ```
- **DO NOT** share your `.env` file on GitHub. Add `.env` to `.gitignore`.

### **5️⃣ Run the Application**

```sh
streamlit run frontend.py
```

🌟 Open the browser at `` to interact with your chatbot.

---

## **📂 Project Structure**

```
/personalized-chatbot
│-- frontend.py          # Streamlit UI for chatbot interaction
│-- backend.py           # Handles API calls to Cohere
│-- .env                 # API keys (DO NOT SHARE)
│-- requirements.txt      # Python dependencies
│-- README.md            # Project documentation
```

---

## **🖥️ How It Works**

1️⃣ **User enters a message** in the input box.\
2️⃣ **Frontend sends input** to `backend.py`.\
3️⃣ **Cohere API processes the input** and generates a response.\
4️⃣ **The response is displayed** in the Streamlit UI.

---

## **🔗 Cohere API Setup**

- Sign up at [Cohere AI](https://cohere.com/)
- Get your API key from the **Cohere dashboard**
- Add it to your `.env` file

---

## **📜 License**

This project is licensed under the **MIT License**. Feel free to use and modify it.

---

## **👨‍💻 Author**

✉️ **Your Name**\
🔗 [LinkedIn](https://www.linkedin.com/in/chinmay-sumbe/)\
🐙 [GitHub](https://github.com/ChinmaySumbe)

---

### **🌟 If you like this project, give it a ⭐ on GitHub!**

