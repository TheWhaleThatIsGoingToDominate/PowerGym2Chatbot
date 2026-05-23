dictionary = {
        "hours":"24 hours a day 7 days a week",
        "available memberships":" 15 months for 3,000 EGP, and 20 months for 3,500 EGP",
        "free trial":"to be confirmed",
        "offerings":("Jazzercise, Aerobics, Zumba, Kickboxing, Bodybuilding coaching, Personal Training, Nutrition Consulting".split(", ")),
        "dedicated section for women":"yes",
        "power gym 2 location":": X432+5X3، البوابة الثالثة، متفرع, Al Haram, Giza Governorate 3510125",
        "contact":"reach us by phone at 01029651505, or contact our manager Hussein at 01151017225",
    }
def chatbot_reply(user_input):

    user_input = user_input.lower().strip()

    for key in dictionary:
        if key == "hours" and ("hours" in user_input or "open" in user_input or "time" in user_input):
            return f"We are open {dictionary.get(key)}."

        elif key == "available memberships" and ("membership" in user_input or "memberships" in user_input or "price" in user_input or "offer" in user_input or "cost" in user_input):
            return f"Our available membership offers are: {dictionary.get(key)}."

        elif key == "free trial" and ("free trial" in user_input or "trial" in user_input):
            return f"The free trial option is currently {dictionary.get(key)}."

        elif key == "offerings" and ("classes" in user_input or "services" in user_input or "offerings" in user_input or "training" in user_input or "zumba" in user_input or "aerobics" in user_input or "kickboxing" in user_input):
            offerings = ", ".join(dictionary.get(key))
            return f"Power Gym currently offers: {offerings}."

        elif key == "dedicated section for women" and ("women" in user_input or "ladies" in user_input or "female" in user_input or "girls" in user_input):
            return f"Yes, Power Gym has a dedicated section for women."

        elif key == "power gym 2 location" and ("location" in user_input or "address" in user_input or "where" in user_input):
            return f"Power Gym 2 is located at: {dictionary.get(key)}."

        elif key == "contact" and ("contact" in user_input or "phone" in user_input or "number" in user_input or "call" in user_input or "manager" in user_input):
            return f"You can {dictionary.get(key)}."

    return "I am not sure about that yet. Please contact Power Gym directly for more details."

