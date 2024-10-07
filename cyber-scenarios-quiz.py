import streamlit as st

# Threat data - dictionary containing threat names, descriptions, and scenarios
cyber_threats = {
    "DDoS (Distributed Denial of Service)": {
        "description": "A DDoS attack aims to overwhelm a network, service, or server with an excessive amount of traffic, rendering it inoperable.",
        "scenario": "Your company’s website is flooded with excessive traffic, causing it to crash. What should you do?",
        "choices": [
            "A) Increase server capacity to handle more traffic.",
            "B) Monitor the traffic sources and block malicious IP addresses.",
            "C) Shut down the website temporarily."
        ],
        "correct": 1,  # B is the correct answer
        "explanation": "The best response is to monitor the traffic and block malicious IP addresses. Increasing server capacity won’t stop the attack, and shutting down the website should be a last resort."
    },
    "Malware": {
        "description": "Malware is a malicious software designed to disrupt, damage, or gain unauthorized access to a computer system.",
        "scenario": "Your colleague accidentally downloads a suspicious file, and now their computer is behaving strangely. What should you do?",
        "choices": [
            "A) Reboot the system.",
            "B) Run an antivirus scan and disconnect the system from the network.",
            "C) Ignore it and continue working."
        ],
        "correct": 1,  # B is the correct answer
        "explanation": "Running an antivirus scan and disconnecting the system from the network can help isolate and remove the malware."
    },
    "Ransomware": {
        "description": "Ransomware encrypts your data and demands payment for its release.",
        "scenario": "Your company’s files are encrypted, and a ransom note demands payment in cryptocurrency to regain access. What should you do?",
        "choices": [
            "A) Pay the ransom to regain access to the files.",
            "B) Restore files from backup and inform authorities.",
            "C) Try to decrypt the files yourself."
        ],
        "correct": 1,  # B is the correct answer
        "explanation": "The best response is to restore files from backups if available and report the attack. Paying the ransom is risky as it does not guarantee file recovery."
    },
    "Man-in-the-Middle Attack": {
        "description": "A Man-in-the-Middle attack involves an attacker intercepting communication between two parties without their knowledge.",
        "scenario": "You’re accessing a public Wi-Fi network, and you suspect someone might be intercepting your communication. What should you do?",
        "choices": [
            "A) Disconnect from the network and use a VPN.",
            "B) Ignore it and continue browsing.",
            "C) Change your passwords immediately."
        ],
        "correct": 0,  # A is the correct answer
        "explanation": "Disconnecting from the public Wi-Fi and using a VPN provides a secure connection, preventing any interception."
    }
}

# Streamlit UI
st.title("Cybersecurity Threat Library")

st.sidebar.header("Select an Attack Type")
# Add a "Select a threat" option as the default
threat_options = ["Select a threat"] + list(cyber_threats.keys())
threat = st.sidebar.selectbox("Choose a threat to learn more", threat_options)

# Check if a valid threat is selected
if threat != "Select a threat":
    # Display threat description
    st.subheader(f"Threat: {threat}")
    st.write(cyber_threats[threat]["description"])

    # Scenario and choices
    st.subheader("Scenario:")
    st.write(cyber_threats[threat]["scenario"])

    # Choices for user
    choices = cyber_threats[threat]["choices"]
    selected_choice = st.radio("What would you do?", choices)

    # Check the answer
    if st.button("Submit"):
        # Get the correct choice index
        correct_answer = cyber_threats[threat]["correct"]
        explanation = cyber_threats[threat]["explanation"]

        if selected_choice == choices[correct_answer]:
            st.success("Correct! 🎉")
        else:
            st.error("Incorrect. 😢")

        # Show the explanation
        st.write(f"**Explanation:** {explanation}")
else:
    # Display a message when no threat is selected
    st.write("Please select a threat from the sidebar to learn more about it.")
