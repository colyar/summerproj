#lists for the dates
aries_list = ["0321","0322","0323","0324","0325","0326","0327","0328","0329","0330","0331","0401","0402","0403","0404","0405","0406","0407","0408","0409","0410","0411","0412","0413","0414","0415","0416","0417","0418","0419"]
taurus_list = ["0420","0421","0422","0423","0424","0425","0426","0427","0428","0429","0430","0431","0501","0502","0503","0504","0506","0507","0508","0509","0510","0511","0512","0513","0514","0515","0516","0517","0518","0519","0520"]
gemini_list = ["0521", "0522", "0523", "0524", "0525", "0526", "0527", "0528", "0529", "0530", "0531", "0601", "0602", "0603", "0604", "0605", "0606", "0607", "0608", "0609", "0610", "0611", "0612", "0613", "0614", "0615", "0616", "0617", "0618", "0619", "0620"]
cancer_list = ["0621", "0622", "0623", "0624", "0625", "0626", "0627", "0628", "0629", "0630", "0631", "0701", "0702", "0703", "0704", "0705", "0706", "0707", "0708", "0709", "0710", "0711", "0712", "0713", "0714", "0715", "0716", "0717", "0718", "0719", "0720", "0721", "0722"]
leo_list = ["0723", "0724", "0725", "0726", "0727", "0728", "0729", "0730", "0731", "0801", "0802", "0803", "0804", "0805", "0806", "0807", "0808", "0809", "0810", "0811", "0812", "0813", "0814", "0815", "0816", "0817", "0818", "0819", "0820", "0821", "0822"]
virgo_list = ["0823", "0824", "0825", "0826", "0827", "0828", "0829", "0830", "0831", "0901", "0902", "0903", "0904", "0905", "0906", "0907", "0908", "0909", "0910", "0911", "0912", "0913", "0914", "0915", "0916", "0917", "0918", "0919", "0920","0921", "0922"]
libra_list = ["0923", "0924", "0925", "0926", "0927", "0928", "0929", "0930", "0931", "1001", "1002", "1003", "1004", "1005", "1006", "1007", "1008", "1009", "1010", "1011", "1012", "1013", "1014", "1015", "1016", "1017", "1018", "1019", "1020","1021", "1022"]
scorpio_list = ["1023", "1024", "1025", "1026", "1027", "1028", "1029", "1030", "1031", "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108", "1109", "1110", "1111", "1112", "1113", "1114", "1115", "1116", "1117", "1118", "1119", "1120","1121"]
sagittarius_list = ["1122", "1123", "1124", "1125", "1126", "1127", "1128", "1129", "1130", "1131", "1201", "1202", "1203", "1204", "1205", "1206", "1207", "1208", "1209", "1210", "1211", "1212", "1213", "1214", "1215", "1216", "1217", "1218", "1219", "1220", "1221" ]
capricorn_list = ["1222", "1223", "1224", "1225", "1226", "1227", "1228", "1229", "1230", "1231", "0101", "0102", "0103", "0104", "0105", "0106", "0107", "0108", "0109", "0110", "0111", "0112", "0113", "0114", "0115", "0116", "0117", "0118", "0119"]
aquarius_list = ["0120", "0121", "0123", "0124", "0125", "0126", "0127", "0128", "0129", "0130", "0131", "0201", "0202", "0203", "0204", "0205", "0206", "0207", "0208", "0209", "0210", "0211", "0212", "0213", "0214", "0215", "0216", "0217", "0218"]
pisces_list = ["0219", "0220", "0221", "0222", "0223", "0224", "0225", "0226", "0227", "0228", "0229", "0230", "0231", "0301", "0302", "0303", "0304", "0305", "0306", "0307", "0308", "0309", "0310", "0311", "0312", "0313", "0314", "0315", "0316", "0317", "0318", "0319", "0321"]
#introduction
name = input("hello! What is your name")
print(
    "hello",
    name,
)
print("Do you want to know")
print("your horoscope? :)")
one = input("Please answer yes,no.")
#define what to do if answer is yes, no,,something else
#still need to add the if answer isnt yes or no/elif
if one == "yes":
    print("great!!")
    birthday = input("Please input your birthday in the mmdd format")
    if birthday.isdigit() == True:
      #aries dates
      if birthday in aries_list:
        print("You are an aries")
        print("Aug 20, 2018 - Step out of your usual role," ,name,". Doing this every now and then can add knowledge and expand your life. The day's planetary aspects favor such growth. Your willingness to walk a different path can give you far more than you imagine. Try something you've never considered before. Go to a new place. Change your desk around. See what you can discover about yourself and the world.")
    if birthday.isdigit() == True:
      #taurus dates
      if birthday in taurus_list:
        print("You are a taurus")
        print("Aug 20, 2018 - Are you satisfied with your current career,",name,"? If not, start by making a plan. There are specific steps that you can take to give you the greatest advantage in the opportunities available. Consider visiting online career sites. There are wonderful articles and tips for the taking. Don't settle for less than you deserve. See what's out there and find a more fulfilling career.")
    if birthday.isdigit() == True:
      #gemini dates
      if birthday in gemini_list:
        print("You are a gemini")
        print("Aug 20, 2018 - Don't fear change,", name,". Even if you think you don't adjust well, you have far more adaptability than you realize. Without change, life would become stagnant and lifeless. It wouldn't be long before you grew unsatisfied and bored with the same old thing. Try to see change as an adventure and a gateway to greater happiness and fulfillment. Trust in your versatility, too.")
    if birthday.isdigit() == True:
      #cancer dates
      if birthday in cancer_list:
        print("You are a cancer")
        print("Aug 20, 2018 - Make your dreams valuable tools for insight,",name,". Back in the old days, great rulers believed so strongly in the insight of dreams that they employed interpreters. Whether you think dreams are mystical insights or random thoughts, you can gain a lot from them. Reoccurring dreams are significant and can point to something that needs addressing. Consider exploring this area.")
    if birthday.isdigit() == True:
      #leo dates
      if birthday in leo_list:
        print("You are a leo")
        print("Aug 20, 2018 - Follow your instincts",name,". Even if you have a tendency to listen more to your reason, put that aside. While your ears can hear words, your intuition can hear what's between the lines and provide you with a much bigger picture. If something sounds right but feels wrong, you'll be better off trusting your feelings. Act with careful consideration and caution.")
    if birthday.isdigit() == True:
      #virgo dates
      if birthday in virgo_list:
        print("You are a virgo")
        print("Aug 20, 2018 - Feed your mind with new knowledge,",name,". Visit a bookstore or read some interesting information online. If you have more time, visit the library or explore courses that you might like. There is knowledge to be had everywhere you look, provided you're open to receiving it. People are often the best resource. Ask someone to explain something, if that's what you need.")
    if birthday.isdigit() == True:
      #libra dates
      if birthday in libra_list:
        print("You are a libra")
        print("Aug 20, 2018 - Try to see nightmares as safe ways to understand feelings,",name,". No one likes to experience them, and we'd sooner forget them once awake, the quickest way to ensure they don't return is to understand what they're saying. Fear, pain, and anxiety are the most common ingredients of nightmares. What frightens you? Do you feel insecure? Consider the questions and probe for answers.")
    if birthday.isdigit() == True:
      #Scorpio dates
      if birthday in scorpio_list:
        print("You are a scorpio")
        print('Aug 20, 2018 - Are you living your dreams,',name,'? Are you still in touch with them? The energy from todays planetary aspects can lend strength and encouragement to this part of your life. Take hold of the things you want most of all. Ask yourself, "What do I want people to say about me when Im gone?" Get back on the road to a fulfilled life by taking steps toward your desires.')
    if birthday.isdigit() == True:
      #sagittarius dates
      if birthday in sagittarius_list:
        print("You are a sagittarius")
        print("Aug 20, 2018 - Today's a good day to check into advancing your career or education,",name,". The energy favors expansion and growth. When was the last time you learned a new skill? It doesn't have to be work related, either. If arranging flowers, skydiving, or proramming websites is something that appeals to you, go for it. Never stop looking for ways to expand your knowledge")
    if birthday.isdigit() == True:
      #capricorn dates
      if birthday in capricorn_list:
        print("You are a capricorn")
        print("Aug 20, 2018 - Do you recognize your intuition as a valuable asset,",name,"? Some people do and some don't. Which group are you in? It can be easy to trust more in concrete, factual reality than in the things you can't touch, yet your intuition can serve you more than you may realize. That gut feeling you experience can guide you toward greatness and alert you to danger. Trust it more.")
    if birthday.isdigit() == True:
      #aquarius dates
      if birthday in aquarius_list:
        print("You are an aquarius")
        print("Aug 20, 2018 - Use your creativity to make things happen today,",name,". This doesn't have to take the form of a finished product. You can come up with new and innovative ways to approach a task, project, or problem. Trust your ability to discover such things. You're known for your sharp thinking and creative abilities. Combining them can make you unstoppable when finding solutions to almost any problem.")
    if birthday.isdigit() == True:
      #pisces dates
      if birthday in pisces_list:
        print("You are a pisces")
        print("Aug 20, 2018 - Find new ways to expand your horizons,",name,". The web has an infinite number of resources and information to explore. Not only that, but your community and local colleges offer various courses to choose from. Think about what you'd enjoy learning - perhaps a new job skill or craft. Whether it's judo or Italian or woodworking that strikes your fancy, it's out there. Find it.")
    if birthday.isdigit() == False:
        print("You did it wrong start over.")
    if one == "no":
        print("k bye")
