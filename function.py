dictionary = {
    "welcome": "Hello! How can I help you today?",
    "welcome_ar": "اهلا بيك، اقدر اساعدك ازاي النهارده؟",
    "hours": "24 hours a day 7 days a week",
    "available memberships": "15 months for 3,000 EGP, and 20 months for 3,500 EGP",
    "free trial": "to be confirmed",
    "offerings": "Jazzercise, Aerobics, Zumba, Kickboxing, Bodybuilding coaching, Personal Training, Nutrition Consulting".split(", "),
    "dedicated section for women": "yes",
    "power gym 2 location": "X432+5X3، البوابة الثالثة، متفرع, Al Haram, Giza Governorate 3510125",
    "contact": "reach us by phone at 01029651505, or contact our manager Hussein at 01151017225",
    "gratitude": "No problem! We are at your service.",
    "gratitude_ar": "العفو، تحت أمرك في أي وقت."
}


def chatbot_reply(user_input):
    user_input = str(user_input).lower().strip()

    for key in dictionary:

        if key == "welcome" and (
            "hello" in user_input
            or "hi" in user_input
            or "hey" in user_input
            or "good morning" in user_input
            or "good evening" in user_input
            or "good afternoon" in user_input
            or "start" in user_input
            or "help" in user_input
        ):
            return dictionary.get(key)

        elif key == "welcome_ar" and (
            "اهلا" in user_input
            or "أهلا" in user_input
            or "اهلاً" in user_input
            or "أهلاً" in user_input
            or "السلام عليكم" in user_input
            or "سلام عليكم" in user_input
            or "ازيك" in user_input
            or "إزيك" in user_input
            or "ازيكوا" in user_input
            or "ازيكو" in user_input
            or "عامل ايه" in user_input
            or "عاملين ايه" in user_input
            or "صباح الخير" in user_input
            or "مساء الخير" in user_input
            or "هاي" in user_input
            or "هالو" in user_input
            or "ممكن مساعدة" in user_input
            or "محتاج مساعدة" in user_input
        ):
            return dictionary.get(key)

        elif key == "hours" and (
            "hours" in user_input
            or "open" in user_input
            or "opening" in user_input
            or "time" in user_input
            or "times" in user_input
            or "when are you open" in user_input
            or "opening hours" in user_input
        ):
            return f"We are open {dictionary.get(key)}."

        elif key == "hours" and (
            "المواعيد" in user_input
            or "مواعيد" in user_input
            or "بتفتحوا" in user_input
            or "بتفتح" in user_input
            or "بتفتحو" in user_input
            or "فاتحين" in user_input
            or "فاتح" in user_input
            or "بتقفلوا" in user_input
            or "بتقفل" in user_input
            or "بتقفلو" in user_input
            or "امتى" in user_input
            or "إمتى" in user_input
            or "الساعه كام" in user_input
            or "الساعة كام" in user_input
            or "شغالين امتى" in user_input
            or "شغالين إمتى" in user_input
            or "مفتوح امتى" in user_input
            or "مفتوح إمتى" in user_input
        ):
            return f"احنا شغالين {dictionary.get(key)}."

        elif key == "available memberships" and (
            "membership" in user_input
            or "memberships" in user_input
            or "price" in user_input
            or "prices" in user_input
            or "offer" in user_input
            or "offers" in user_input
            or "cost" in user_input
            or "how much" in user_input
            or "plans" in user_input
            or "packages" in user_input
        ):
            return f"Our available membership offers are: {dictionary.get(key)}."

        elif key == "available memberships" and (
            "بكام" in user_input
            or "كام" in user_input
            or "السعر" in user_input
            or "الاسعار" in user_input
            or "الأسعار" in user_input
            or "اسعار" in user_input
            or "أسعار" in user_input
            or "العروض" in user_input
            or "عروض" in user_input
            or "ايه العروض" in user_input
            or "إيه العروض" in user_input
            or "اية العروض" in user_input
            or "ايه الاسعار" in user_input
            or "ايه الأسعار" in user_input
            or "إيه الأسعار" in user_input
            or "الاشتراك" in user_input
            or "اشتراك" in user_input
            or "العضوية" in user_input
            or "عضوية" in user_input
            or "الشهر بكام" in user_input
            or "السنة بكام" in user_input
            or "كام الاشتراك" in user_input
            or "الاشتراك بكام" in user_input
            or "العضوية بكام" in user_input
        ):
            return f"العروض المتاحة حاليا: {dictionary.get(key)}."

        elif key == "free trial" and (
            "free trial" in user_input
            or "trial" in user_input
            or "try" in user_input
            or "can i try" in user_input
            or "trial session" in user_input
        ):
            return f"The free trial option is currently {dictionary.get(key)}."

        elif key == "free trial" and (
            "تجربة مجانية" in user_input
            or "تجربه مجانيه" in user_input
            or "تجربة ببلاش" in user_input
            or "تجربه ببلاش" in user_input
            or "ينفع اجرب" in user_input
            or "ينفع أجرب" in user_input
            or "اجرب الاول" in user_input
            or "أجرب الأول" in user_input
            or "فيه تجربة" in user_input
            or "في تجربة" in user_input
            or "فيه ترايل" in user_input
            or "في ترايل" in user_input
            or "ترايل" in user_input
        ):
            return f"موضوع التجربة المجانية حاليا {dictionary.get(key)}."

        elif key == "offerings" and (
            "classes" in user_input
            or "services" in user_input
            or "offerings" in user_input
            or "training" in user_input
            or "zumba" in user_input
            or "aerobics" in user_input
            or "kickboxing" in user_input
            or "personal training" in user_input
            or "nutrition" in user_input
            or "coaching" in user_input
            or "what do you offer" in user_input
            or "what services" in user_input
        ):
            offerings = ", ".join(dictionary.get(key))
            return f"Power Gym currently offers: {offerings}."

        elif key == "offerings" and (
            "الخدمات" in user_input
            or "خدمات" in user_input
            or "ايه الخدمات" in user_input
            or "إيه الخدمات" in user_input
            or "اية الخدمات" in user_input
            or "ايه اللي عندكم" in user_input
            or "ايه الي عندكم" in user_input
            or "إيه اللي عندكم" in user_input
            or "ايه اللي عندكوا" in user_input
            or "ايه الي عندكوا" in user_input
            or "ايه اللي عندكو" in user_input
            or "ايه الي عندكو" in user_input
            or "عندكم ايه" in user_input
            or "عندكوا ايه" in user_input
            or "عندكو ايه" in user_input
            or "فيه ايه" in user_input
            or "في ايه" in user_input
            or "ايه الموجود" in user_input
            or "بتقدمو ايه" in user_input
            or "بتقدموا ايه" in user_input
            or "بتقدمو اي" in user_input
            or "بتقدموا اي" in user_input
            or "ايه الانشطة" in user_input
            or "ايه الأنشطة" in user_input
            or "انشطة" in user_input
            or "أنشطة" in user_input
            or "زومبا" in user_input
            or "ايروبكس" in user_input
            or "أيروبكس" in user_input
            or "كيك بوكسينج" in user_input
            or "كيكبوكسينج" in user_input
            or "تدريب شخصي" in user_input
            or "تغذية" in user_input
            or "كمال اجسام" in user_input
            or "كمال أجسام" in user_input
        ):
            offerings = ", ".join(dictionary.get(key))
            return f"عندنا في باور جيم: {offerings}."

        elif key == "dedicated section for women" and (
            "women" in user_input
            or "ladies" in user_input
            or "female" in user_input
            or "girls" in user_input
            or "women section" in user_input
            or "ladies section" in user_input
            or "girls section" in user_input
        ):
            return "Yes, Power Gym has a dedicated section for women."

        elif key == "dedicated section for women" and (
            "بنات" in user_input
            or "سيدات" in user_input
            or "نساء" in user_input
            or "حريمي" in user_input
            or "للبنات" in user_input
            or "للسيدات" in user_input
            or "قسم بنات" in user_input
            or "قسم للسيدات" in user_input
            or "قسم حريمي" in user_input
            or "فيه بنات" in user_input
            or "في بنات" in user_input
            or "فيه قسم بنات" in user_input
            or "في قسم بنات" in user_input
            or "فيه قسم للسيدات" in user_input
            or "في قسم للسيدات" in user_input
        ):
            return "ايوه، في باور جيم فيه قسم مخصص للسيدات."

        elif key == "power gym 2 location" and (
            "location" in user_input
            or "address" in user_input
            or "where" in user_input
            or "where are you" in user_input
            or "where is the gym" in user_input
            or "gym location" in user_input
            or "branch location" in user_input
        ):
            return f"Power Gym 2 is located at: {dictionary.get(key)}."

        elif key == "power gym 2 location" and (
            "فين" in user_input
            or "مكانكم" in user_input
            or "مكانكو" in user_input
            or "مكانكوا" in user_input
            or "العنوان" in user_input
            or "عنوانكم" in user_input
            or "عنوانكو" in user_input
            or "عنوانكوا" in user_input
            or "الجيم فين" in user_input
            or "الفرع فين" in user_input
            or "باور جيم فين" in user_input
            or "مكان الجيم" in user_input
            or "عنوان الجيم" in user_input
            or "موجودين فين" in user_input
            or "انتو فين" in user_input
            or "انتم فين" in user_input
        ):
            return f"باور جيم 2 موجود في: {dictionary.get(key)}."

        elif key == "contact" and (
            "contact" in user_input
            or "phone" in user_input
            or "number" in user_input
            or "call" in user_input
            or "manager" in user_input
            or "whatsapp" in user_input
            or "mobile" in user_input
            or "how can i contact" in user_input
        ):
            return f"You can {dictionary.get(key)}."

        elif key == "contact" and (
            "رقم" in user_input
            or "النمرة" in user_input
            or "نمره" in user_input
            or "تليفون" in user_input
            or "تلفون" in user_input
            or "موبايل" in user_input
            or "واتساب" in user_input
            or "واتس" in user_input
            or "اكلمكم" in user_input
            or "أكلمكم" in user_input
            or "اتواصل" in user_input
            or "أتواصل" in user_input
            or "المدير" in user_input
            or "مدير" in user_input
            or "رقمكم" in user_input
            or "رقمكو" in user_input
            or "رقمكوا" in user_input
            or "نمرتكم" in user_input
            or "نمرتكو" in user_input
            or "نمرتكوا" in user_input
        ):
            return f"تقدر تتواصل معانا كده: {dictionary.get(key)}."

        elif key == "gratitude" and (
            "thank" in user_input
            or "thanks" in user_input
            or "thank you" in user_input
            or "ty" in user_input
            or "tysm" in user_input
            or "appreciate it" in user_input
        ):
            return dictionary.get(key)

        elif key == "gratitude" and (
            "شكرا" in user_input
            or "شكرًا" in user_input
            or "متشكر" in user_input
            or "متشكرة" in user_input
            or "تسلم" in user_input
            or "تسلمي" in user_input
            or "تسلم يا باشا" in user_input
            or "تسلم يسطا" in user_input
            or "ميرسي" in user_input
            or "حبيبي" in user_input
            or "حبيبى" in user_input
            or "تمام شكرا" in user_input
            or "الف شكر" in user_input
            or "ألف شكر" in user_input
            or "الف شكر ليكم" in user_input
            or "متشكرين" in user_input
        ):
            return dictionary.get("gratitude_ar")

    english_letters = "abcdefghijklmnopqrstuvwxyz"
    arabic_letters = "ابتثجحخدذرزسشصضطظعغفقكلمنهويأإآةىؤئ"

    engFlag = False
    arFlag = False

    for letter in user_input:
        if letter in english_letters:
            engFlag = True

        elif letter in arabic_letters:
            arFlag = True

    if arFlag and not engFlag:
        return "مش متأكد من الإجابة على السؤال ده حاليا. ممكن تتواصل مع باور جيم مباشرة لمزيد من التفاصيل."

    return "I am not sure about that yet. Please contact Power Gym directly for more details."