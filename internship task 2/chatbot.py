print("Hello! I am a simple chatbot for Smart Trainers.")
    
   
responses = {
        ("courses", "programs", "offer","course","programming"): "We offer: Freelancing, AutoCAD, Graphic Designing, UI/UX, Web Dev, and Python programming",

        ("registration", "apply","next","upcoming","future", "register"): "Registrations for Batch 03 are open! It is an 8-week program.here is the link : https://docs.google.com/forms/d/e/1FAIpQLSdQOTx2ILF1afZz-hK7dGNYFP2dYFt6r32FrPKoMusSr4XbxA/viewform?usp=header",
        
        ("start", "duration",  "long"): "Batch 03 is 8 weeks long and starts soon.",

        ("batch", "program", "internship", "current", "running", "going","ongoing"): "We are currently in the Remote Internship (Batch-02).",

        ("founded", "year", "found", "history"): "Smart Trainers was founded in 2025.",
    
        ("name", "company"): "Smart Trainers",

        ("location", "address", "where", "located"): "Elsa Qazi Campus (Old Campus), Colony, Thandi Sarak, Hyderabad (Sindh), Pakistan.",

        ("business", "work"): "Professional Training & Internships",

        ("specialization", "specialize", "expert"): "Computer Science, Programming (Python), Artificial Intelligence, and Skill Development",

        ("activities", "task"): "Hands-on technical tasks (e.g., Command Line Interface apps,  E-commerce logic)",

        ("mission", "aim", "goal"): "To bridge the gap between academic learning and industry skills.",

        ("linkedin", "link"): "https://www.linkedin.com/company/smarttrainers/",

        ("schedule", "timing", "time"): "Classes are held on Friday, Saturday, and Sunday evenings.",

        ("contact", "phone", "email", "gmail", "whatsapp", "number"): "WhatsApp: +92 312 0279418 or Email: info.smarttrainers@gmail.com",

        ("vision",): "To become the leading platform in Pakistan for industry-ready engineers.",
        
        ("size", "employees"): "We have 11-50 employees.",
        
        ("about", "about us", "intro", "introduction", "overview", "who are you"): "Smart Trainers is dedicated to transforming engineering education into real-world career readiness. We go beyond textbooks, empowering students with hands-on skills and internship opportunities to make them truly industry-ready.",

        ("hi", "hello", "salam", "hey"): "Hello! How can I help you?",
    }

list_for_unknown_questions = []

    
while True:                   #  Starting the infinite loop so the chat keeps going
        ask = input("\nTell me how can I assist you: ").strip().lower()

        if ask == "bye":          #  Checking if the user wants to quit
            print("Goodbye! Have a nice day.")
            break 

        

        ask = ask.replace("?", "").replace("!", "").replace(".", "").replace(",", "")    #  Cleaning the input: Removing punctuation marks (?, !, .)

        #  The "Space trick": Adding spaces to start and end
        # This turns "who are they" into " who are they "
        # It helps us distinguish whole words like "hey" vs "they"

        padded_ask = " " + ask + " "

        found_answer = False
        
        
        for keywords_tuple, answer in responses.items():  #  Looping through our dictionary

            # 'keywords_tuple' is group of keys 

            
            for keyword in keywords_tuple:             # Checking each specific keyword (synonym) in the group

                padded_keyword = " " + keyword + " "    # Adding spaces to the keyword too


                if padded_keyword in padded_ask:      #  Checking if the whole word exists in the user's sentence
                    print(f"Chatbot response: {answer}")
                    found_answer = True
                

                    break                         # Stop looking at other keywords in this group
            
            if found_answer:
                break             # Stop looking at other response groups if we found one
        
        if not found_answer:
            list_for_unknown_questions.append(ask)

            print("Sorry, I don't know the answer to that yet.")

print(" List of unknown questions user asked : ")
print(list_for_unknown_questions)

