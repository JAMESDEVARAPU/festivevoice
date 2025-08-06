"""
Translation system for the Indian Cultural Corpus Collection App.
Supports multiple Indian languages with culturally appropriate translations.
"""

# Supported languages with their native names
SUPPORTED_LANGUAGES = {
    'English': 'English',
    'हिन्दी (Hindi)': 'Hindi',
    'বাংলা (Bengali)': 'Bengali',
    'தமிழ் (Tamil)': 'Tamil',
    'తెలుగు (Telugu)': 'Telugu',
    'मराठी (Marathi)': 'Marathi',
    'ગુજરાતી (Gujarati)': 'Gujarati',
    'ಕನ್ನಡ (Kannada)': 'Kannada',
    'മലയാളം (Malayalam)': 'Malayalam',
    'ਪੰਜਾਬੀ (Punjabi)': 'Punjabi',
    'ଓଡିଆ (Odia)': 'Odia'
}

# Translation dictionary with culturally appropriate terms
TRANSLATIONS = {
    'English': {
        'title': 'Indian Cultural Heritage Explorer',
        'subtitle': 'Discover, Learn, and Contribute to India\'s Rich Cultural Legacy',
        'welcome_title': 'Welcome to Our Cultural Journey',
        'welcome_message': 'Join us in preserving and sharing India\'s incredible cultural diversity. Your contributions help build a comprehensive knowledge base for future generations.',
        'community_title': 'Building Cultural Bridge Together',
        'community_message': 'Every story, word, and tradition you share enriches our collective understanding of Indian heritage. Together, we create a living repository of cultural wisdom.',
        'data_usage_note': 'All contributions are used respectfully for educational and cultural preservation purposes.',
        'contribute_now': 'Contribute Now',
        'explore_culture': 'Explore Culture',
        'your_contributions': 'Your Contributions',
        'recent_activity': 'Recent Community Activity',
        'quality_content': 'Quality Cultural Content',
        'diverse_languages': 'Diverse Languages Represented',
        'cultural_categories': 'Cultural Categories Covered'
    },
    
    'Hindi': {
        'title': 'भारतीय सांस्कृतिक विरासत अन्वेषक',
        'subtitle': 'भारत की समृद्ध सांस्कृतिक विरासत की खोज करें, सीखें और योगदान दें',
        'welcome_title': 'हमारी सांस्कृतिक यात्रा में आपका स्वागत है',
        'welcome_message': 'भारत की अविश्वसनीय सांस्कृतिक विविधता को संरक्षित और साझा करने में हमारे साथ जुड़ें। आपके योगदान भविष्य की पीढ़ियों के लिए एक व्यापक ज्ञान आधार बनाने में मदद करते हैं।',
        'community_title': 'मिलकर सांस्कृतिक सेतु का निर्माण',
        'community_message': 'आप जो भी कहानी, शब्द और परंपरा साझा करते हैं, वह भारतीय विरासत की हमारी सामूहिक समझ को समृद्ध बनाती है। मिलकर हम सांस्कृतिक ज्ञान का एक जीवंत भंडार बनाते हैं।',
        'data_usage_note': 'सभी योगदानों का उपयोग शैक्षिक और सांस्कृतिक संरक्षण उद्देश्यों के लिए सम्मानपूर्वक किया जाता है।',
        'contribute_now': 'अभी योगदान दें',
        'explore_culture': 'संस्कृति की खोज करें',
        'your_contributions': 'आपके योगदान',
        'recent_activity': 'समुदाय की हाल की गतिविधि',
        'quality_content': 'गुणवत्तापूर्ण सांस्कृतिक सामग्री',
        'diverse_languages': 'विविध भाषाओं का प्रतिनिधित्व',
        'cultural_categories': 'सांस्कृतिक श्रेणियां शामिल'
    },
    
    'Bengali': {
        'title': 'ভারতীয় সাংস্কৃতিক ঐতিহ্য অন্বেষক',
        'subtitle': 'ভারতের সমৃদ্ধ সাংস্কৃতিক ঐতিহ্য আবিষ্কার, শেখা এবং অবদান রাখুন',
        'welcome_title': 'আমাদের সাংস্কৃতিক যাত্রায় স্বাগতম',
        'welcome_message': 'ভারতের অবিশ্বাস্য সাংস্কৃতিক বৈচিত্র্য সংরক্ষণ ও ভাগাভাগিতে আমাদের সাথে যোগ দিন। আপনার অবদান ভবিষ্যত প্রজন্মের জন্য একটি বিস্তৃত জ্ঞানভিত্তিক গড়তে সাহায্য করে।',
        'community_title': 'একসাথে সাংস্কৃতিক সেতু নির্মাণ',
        'community_message': 'আপনি যে প্রতিটি গল্প, শব্দ এবং ঐতিহ্য ভাগ করেন তা ভারতীয় ঐতিহ্য সম্পর্কে আমাদের সামষ্টিক বোঝাপড়াকে সমৃদ্ধ করে। একসাথে আমরা সাংস্কৃতিক জ্ঞানের একটি জীবন্ত ভাণ্ডার তৈরি করি।',
        'data_usage_note': 'সমস্ত অবদান শিক্ষামূলক এবং সাংস্কৃতিক সংরক্ষণের উদ্দেশ্যে সম্মানজনকভাবে ব্যবহৃত হয়।',
        'contribute_now': 'এখনই অবদান রাখুন',
        'explore_culture': 'সংস্কৃতি অন্বেষণ করুন',
        'your_contributions': 'আপনার অবদান',
        'recent_activity': 'সম্প্রদায়ের সাম্প্রতিক কার্যকলাপ',
        'quality_content': 'গুণগত সাংস্কৃতিক বিষয়বস্তু',
        'diverse_languages': 'বিবিধ ভাষার প্রতিনিধিত্ব',
        'cultural_categories': 'সাংস্কৃতিক বিভাগ অন্তর্ভুক্ত'
    },
    
    'Tamil': {
        'title': 'இந்திய கலாச்சார பாரம்பரிய ஆய்வாளர்',
        'subtitle': 'இந்தியாவின் வளமான கலாச்சார மரபுகளை கண்டுபிடித்து, கற்றுக்கொண்டு, பங்களிக்கவும்',
        'welcome_title': 'எங்கள் கலாச்சார பயணத்திற்கு வரவேற்கிறோம்',
        'welcome_message': 'இந்தியாவின் நம்பமுடியாத கலாச்சார பன்முகத்தன்மையை பாதுகாத்து பகிர்ந்துகொள்வதில் எங்களுடன் சேரவும். உங்கள் பங்களிப்புகள் எதிர்கால சந்ததியினருக்காக ஒரு விரிவான அறிவுத் தளத்தை உருவாக்க உதவுகின்றன.',
        'community_title': 'ஒன்றாக கலாச்சார பாலம் கட்டுதல்',
        'community_message': 'நீங்கள் பகிர்ந்துகொள்ளும் ஒவ்வொரு கதை, சொல் மற்றும் பாரம்பரியமும் இந்திய பாரம்பரியத்தைப் பற்றிய நமது கூட்டு புரிதலை வளப்படுத்துகிறது. ஒன்றாக நாம் கலாச்சார ஞானத்தின் வாழும் கருவூலத்தை உருவாக்குகிறோம்.',
        'data_usage_note': 'அனைத்து பங்களிப்புகளும் கல்வி மற்றும் கலாச்சார பாதுகாப்பு நோக்கங்களுக்காக மரியாதையுடன் பயன்படுத்தப்படுகின்றன.',
        'contribute_now': 'இப்போது பங்களிக்கவும்',
        'explore_culture': 'கலாச்சாரத்தை ஆராயுங்கள்',
        'your_contributions': 'உங்கள் பங்களிப்புகள்',
        'recent_activity': 'சமூகத்தின் சமீபத்திய செயல்பாடு',
        'quality_content': 'தரமான கலாச்சார உள்ளடக்கம்',
        'diverse_languages': 'பல்வேறு மொழிகளின் பிரதிநிதித்துவம்',
        'cultural_categories': 'கலாச்சார வகைகள் சேர்க்கப்பட்டுள்ளன'
    },
    
    'Telugu': {
        'title': 'భారతీయ సాంస్కృతిక వారసత్వ అన్వేషకుడు',
        'subtitle': 'భారతదేశపు గొప్ప సాంస్కృతిక వారసత్వాన్ని కనుగొనండి, నేర్చుకోండి మరియు సహకరించండి',
        'welcome_title': 'మా సాంస్కృతిక యాత్రకు స్వాగతం',
        'welcome_message': 'భారతదేశపు అద్భుతమైన సాంస్కృతిక వైవిధ్యాన్ని సంరక్షించడంలో మరియు పంచుకోవడంలో మాతో చేరండి. మీ సహకారం భవిష్యత్ తరాలకు విస్తృతమైన జ్ఞాన స్థావరాన్ని నిర్మించడంలో సహాయపడుతుంది.',
        'community_title': 'కలిసి సాంస్కృతిక వారధిని నిర్మించడం',
        'community_message': 'మీరు పంచుకునే ప్రతి కథ, పదం మరియు సంప్రదాయం భారతీయ వారసత్వం గురించి మన సమిష్టి అవగాహనను సుసంపన్నం చేస్తుంది. కలిసి మేము సాంస్కృతిక జ్ఞానం యొక్క సజీవ భాండాగారాన్ని సృష్టిస్తాము.',
        'data_usage_note': 'అన్ని సహకారాలు విద్యా మరియు సాంస్కృతిక సంరక్షణ ప్రయోజనాల కోసం గౌరవంగా ఉపయోగించబడతాయి.',
        'contribute_now': 'ఇప్పుడే సహకరించండి',
        'explore_culture': 'సంస్కృతిని అన్వేషించండి',
        'your_contributions': 'మీ సహకారాలు',
        'recent_activity': 'సమాజం యొక్క ఇటీవలి కార్యకలాపాలు',
        'quality_content': 'నాణ్యమైన సాంస్కృతిక కంటెంట్',
        'diverse_languages': 'వైవిధ్యమైన భాషల ప్రాతినిధ్యం',
        'cultural_categories': 'సాంస్కృతిక వర్గాలు చేర్చబడ్డాయి'
    },
    
    'Marathi': {
        'title': 'भारतीय सांस्कृतिक वारसा अन्वेषक',
        'subtitle': 'भारताच्या समृद्ध सांस्कृतिक वारशाचा शोध घ्या, शिका आणि योगदान द्या',
        'welcome_title': 'आमच्या सांस्कृतिक प्रवासात आपले स्वागत आहे',
        'welcome_message': 'भारताची अविश्वसनीय सांस्कृतिक विविधता जतन करण्यात आणि सामायिक करण्यात आमच्यात सामील व्हा. तुमचे योगदान भावी पिढ्यांसाठी व्यापक ज्ञानाचा आधार तयार करण्यास मदत करते.',
        'community_title': 'एकत्रितपणे सांस्कृतिक पूल बांधणे',
        'community_message': 'तुम्ही सामायिक करता ती प्रत्येक गोष्ट, शब्द आणि परंपरा भारतीय वारशाबद्दलची आमची सामूहिक समज समृद्ध करते. एकत्रितपणे आम्ही सांस्कृतिक ज्ञानाचा जिवंत खजिना तयार करतो.',
        'data_usage_note': 'सर्व योगदानांचा उपयोग शैक्षणिक आणि सांस्कृतिक संरक्षण हेतूंसाठी आदरपूर्वक केला जातो.',
        'contribute_now': 'आत्ता योगदान द्या',
        'explore_culture': 'संस्कृतीचा शोध घ्या',
        'your_contributions': 'तुमचे योगदान',
        'recent_activity': 'समुदायाची अलीकडील क्रियाकलाप',
        'quality_content': 'दर्जेदार सांस्कृतिक मजकूर',
        'diverse_languages': 'विविध भाषांचे प्रतिनिधित्व',
        'cultural_categories': 'सांस्कृतिक श्रेण्या समाविष्ट'
    },
    
    'Gujarati': {
        'title': 'ભારતીય સાંસ્કૃતિક વારસો અન્વેષક',
        'subtitle': 'ભારતના સમૃદ્ધ સાંસ્કૃતિક વારસાની શોધ કરો, શીખો અને યોગદાન આપો',
        'welcome_title': 'અમારી સાંસ્કૃતિક યાત્રામાં તમારું સ્વાગત છે',
        'welcome_message': 'ભારતની અવિશ્વસનીય સાંસ્કૃતિક વિવિધતાને સાચવવામાં અને વહેંચવામાં અમારી સાથે જોડાઓ. તમારું યોગદાન ભાવિ પેઢીઓ માટે વ્યાપક જ્ઞાન આધાર બનાવવામાં મદદ કરે છે.',
        'community_title': 'મળીને સાંસ્કૃતિક પુલ બાંધવું',
        'community_message': 'તમે શેર કરો છો તે દરેક વાર્તા, શબ્દ અને પરંપરા ભારતીય વારસા વિશેની આપણી સામૂહિક સમજને સમૃદ્ધ બનાવે છે. મળીને આપણે સાંસ્કૃતિક જ્ઞાનનું જીવંત ભંડાર બનાવીએ છીએ.',
        'data_usage_note': 'બધું યોગદાન શિક્ષણિક અને સાંસ્કૃતિક સંરક્ષણ હેતુઓ માટે આદરપૂર્વક ઉપયોગમાં લેવાય છે.',
        'contribute_now': 'હવે યોગદાન આપો',
        'explore_culture': 'સંસ્કૃતિનું અન્વેષણ કરો',
        'your_contributions': 'તમારું યોગદાન',
        'recent_activity': 'સમુદાયની તાજેતરની પ્રવૃત્તિ',
        'quality_content': 'ગુણવત્તાપૂર્ણ સાંસ્કૃતિક સામગ્રી',
        'diverse_languages': 'વિવિધ ભાષાઓનું પ્રતિનિધિત્વ',
        'cultural_categories': 'સાંસ્કૃતિક શ્રેણીઓ સામેલ'
    },
    
    'Kannada': {
        'title': 'ಭಾರತೀಯ ಸಾಂಸ್ಕೃತಿಕ ಪರಂಪರೆ ಅನ್ವೇಷಕ',
        'subtitle': 'ಭಾರತದ ಶ್ರೀಮಂತ ಸಾಂಸ್ಕೃತಿಕ ಪರಂಪರೆಯನ್ನು ಅನ್ವೇಷಿಸಿ, ಕಲಿಯಿರಿ ಮತ್ತು ಕೊಡುಗೆ ನೀಡಿ',
        'welcome_title': 'ನಮ್ಮ ಸಾಂಸ್ಕೃತಿಕ ಪ್ರಯಾಣಕ್ಕೆ ನಿಮಗೆ ಸ್ವಾಗತ',
        'welcome_message': 'ಭಾರತದ ಅದ್ಭುತ ಸಾಂಸ್ಕೃತಿಕ ವೈವಿಧ್ಯತೆಯನ್ನು ಸಂರಕ್ಷಿಸಲು ಮತ್ತು ಹಂಚಿಕೊಳ್ಳಲು ನಮ್ಮೊಂದಿಗೆ ಸೇರಿರಿ. ನಿಮ್ಮ ಕೊಡುಗೆಗಳು ಭವಿಷ್ಯದ ಪೀಳಿಗೆಗಳಿಗೆ ಸಮಗ್ರ ಜ್ಞಾನ ಆಧಾರವನ್ನು ನಿರ್ಮಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.',
        'community_title': 'ಒಟ್ಟಿಗೆ ಸಾಂಸ್ಕೃತಿಕ ಸೇತುವೆ ನಿರ್ಮಾಣ',
        'community_message': 'ನೀವು ಹಂಚಿಕೊಳ್ಳುವ ಪ್ರತಿಯೊಂದು ಕಥೆ, ಪದ ಮತ್ತು ಸಂಪ್ರದಾಯವು ಭಾರತೀಯ ಪರಂಪರೆಯ ಬಗ್ಗೆ ನಮ್ಮ ಸಾಮೂಹಿಕ ತಿಳುವಳಿಕೆಯನ್ನು ಶ್ರೀಮಂತಗೊಳಿಸುತ್ತದೆ. ಒಟ್ಟಿಗೆ ನಾವು ಸಾಂಸ್ಕೃತಿಕ ಜ್ಞಾನದ ಜೀವಂತ ಖಜಾನೆಯನ್ನು ರಚಿಸುತ್ತೇವೆ.',
        'data_usage_note': 'ಎಲ್ಲಾ ಕೊಡುಗೆಗಳನ್ನು ಶೈಕ್ಷಣಿಕ ಮತ್ತು ಸಾಂಸ್ಕೃತಿಕ ಸಂರಕ್ಷಣಾ ಉದ್ದೇಶಗಳಿಗಾಗಿ ಗೌರವದಿಂದ ಬಳಸಲಾಗುತ್ತದೆ.',
        'contribute_now': 'ಈಗಲೇ ಕೊಡುಗೆ ನೀಡಿ',
        'explore_culture': 'ಸಂಸ್ಕೃತಿಯನ್ನು ಅನ್ವೇಷಿಸಿ',
        'your_contributions': 'ನಿಮ್ಮ ಕೊಡುಗೆಗಳು',
        'recent_activity': 'ಸಮುದಾಯದ ಇತ್ತೀಚಿನ ಚಟುವಟಿಕೆ',
        'quality_content': 'ಗುಣಮಟ್ಟದ ಸಾಂಸ್ಕೃತಿಕ ವಿಷಯ',
        'diverse_languages': 'ವಿವಿಧ ಭಾಷೆಗಳ ಪ್ರಾತಿನಿಧ್ಯ',
        'cultural_categories': 'ಸಾಂಸ್ಕೃತಿಕ ವರ್ಗಗಳು ಸೇರಿಸಲಾಗಿದೆ'
    },
    
    'Malayalam': {
        'title': 'ഇന്ത്യൻ സാംസ്കാരിക പൈതൃക പര്യവേക്ഷകൻ',
        'subtitle': 'ഇന്ത്യയുടെ സമ്പന്നമായ സാംസ്കാരിക പൈതൃകം കണ്ടെത്തുകയും പഠിക്കുകയും സംഭാവന നൽകുകയും ചെയ്യുക',
        'welcome_title': 'ഞങ്ങളുടെ സാംസ്കാരിക യാത്രയിലേക്ക് സ്വാഗതം',
        'welcome_message': 'ഇന്ത്യയുടെ അവിശ്വസനീയമായ സാംസ്കാരിക വൈവിധ്യം സംരക്ഷിക്കുന്നതിലും പങ്കിടുന്നതിലും ഞങ്ങളുടെ കൂടെ ചേരുക. നിങ്ങളുടെ സംഭാവനകൾ ഭാവി തലമുറകൾക്കായി വിപുലമായ അറിവിന്റെ അടിത്തറ നിർമ്മിക്കാൻ സഹായിക്കുന്നു.',
        'community_title': 'ഒന്നിച്ച് സാംസ്കാരിക പാലം നിർമ്മിക്കുക',
        'community_message': 'നിങ്ങൾ പങ്കിടുന്ന ഓരോ കഥയും വാക്കും പാരമ്പര്യവും ഇന്ത്യൻ പൈതൃകത്തെക്കുറിച്ചുള്ള നമ്മുടെ കൂട്ടായ ധാരണയെ സമ്പന്നമാക്കുന്നു. ഒരുമിച്ച് നാം സാംസ്കാരിക ജ്ഞാനത്തിന്റെ ജീവനുള്ള ഭണ്ডാരം സൃഷ്ടിക്കുന്നു.',
        'data_usage_note': 'എല്ലാ സംഭാവനകളും വിദ്യാഭ്യാസപരവും സാംസ്കാരിക സംരക്ഷണ ആവശ്യങ്ങൾക്കുമായി ബഹുമാനത്തോടെ ഉപയോഗിക്കുന്നു.',
        'contribute_now': 'ഇപ്പോൾ സംഭാവന ചെയ്യുക',
        'explore_culture': 'സംസ്കാരം പര്യവേക്ഷണം ചെയ്യുക',
        'your_contributions': 'നിങ്ങളുടെ സംഭാവനകൾ',
        'recent_activity': 'കമ്മ്യൂണിറ്റിയുടെ സമീപകാല പ്രവർത്തനം',
        'quality_content': 'ഗുണനിലവാരമുള്ള സാംസ്കാരിക ഉള്ളടക്കം',
        'diverse_languages': 'വൈവിധ്യമാർന്ന ഭാഷകളുടെ പ്രാതിനിധ്യം',
        'cultural_categories': 'സാംസ്കാരിക വിഭാഗങ്ങൾ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്'
    },
    
    'Punjabi': {
        'title': 'ਭਾਰਤੀ ਸੱਭਿਆਚਾਰਕ ਵਿਰਾਸਤ ਖੋਜਕਰਤਾ',
        'subtitle': 'ਭਾਰਤ ਦੇ ਅਮੀਰ ਸੱਭਿਆਚਾਰਕ ਵਿਰਾਸਤ ਦੀ ਖੋਜ ਕਰੋ, ਸਿੱਖੋ ਅਤੇ ਯੋਗਦਾਨ ਦਿਓ',
        'welcome_title': 'ਸਾਡੀ ਸੱਭਿਆਚਾਰਕ ਯਾਤਰਾ ਵਿੱਚ ਜੀ ਆਇਆਂ ਨੂੰ',
        'welcome_message': 'ਭਾਰਤ ਦੀ ਅਦਭੁਤ ਸੱਭਿਆਚਾਰਕ ਵਿਭਿੰਨਤਾ ਨੂੰ ਸੰਭਾਲਣ ਅਤੇ ਸਾਂਝਾ ਕਰਨ ਵਿੱਚ ਸਾਡੇ ਨਾਲ ਜੁੜੋ। ਤੁਹਾਡੇ ਯੋਗਦਾਨ ਆਉਣ ਵਾਲੀਆਂ ਪੀੜ੍ਹੀਆਂ ਲਈ ਇੱਕ ਵਿਆਪਕ ਗਿਆਨ ਅਧਾਰ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ।',
        'community_title': 'ਮਿਲ ਕੇ ਸੱਭਿਆਚਾਰਕ ਪੁਲ ਬਣਾਉਣਾ',
        'community_message': 'ਤੁਸੀਂ ਸਾਂਝਾ ਕਰਦੀ ਹਰ ਕਹਾਣੀ, ਸ਼ਬਦ ਅਤੇ ਰੀਤ ਭਾਰਤੀ ਵਿਰਾਸਤ ਬਾਰੇ ਸਾਡੀ ਸਮੂਹਿਕ ਸਮਝ ਨੂੰ ਅਮੀਰ ਬਣਾਉਂਦੀ ਹੈ। ਮਿਲ ਕੇ ਅਸੀਂ ਸੱਭਿਆਚਾਰਕ ਗਿਆਨ ਦਾ ਇੱਕ ਜੀਵੰਤ ਖਜ਼ਾਨਾ ਬਣਾਉਂਦੇ ਹਾਂ।',
        'data_usage_note': 'ਸਾਰੇ ਯੋਗਦਾਨਾਂ ਦੀ ਵਰਤੋਂ ਸਿੱਖਿਆਦਾਇਕ ਅਤੇ ਸੱਭਿਆਚਾਰਕ ਸੰਭਾਲ ਦੇ ਮਕਸਦਾਂ ਲਈ ਸਨਮਾਨ ਨਾਲ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।',
        'contribute_now': 'ਹੁਣ ਯੋਗਦਾਨ ਦਿਓ',
        'explore_culture': 'ਸੱਭਿਆਚਾਰ ਦੀ ਖੋਜ ਕਰੋ',
        'your_contributions': 'ਤੁਹਾਡੇ ਯੋਗਦਾਨ',
        'recent_activity': 'ਕਮਿਊਨਿਟੀ ਦੀ ਤਾਜ਼ਾ ਗਤੀਵਿਧੀ',
        'quality_content': 'ਗੁਣਵੱਤਾ ਸੱਭਿਆਚਾਰਕ ਸਮਗਰੀ',
        'diverse_languages': 'ਵਿਭਿੰਨ ਭਾਸ਼ਾਵਾਂ ਦੀ ਨੁਮਾਇੰਦਗੀ',
        'cultural_categories': 'ਸੱਭਿਆਚਾਰਕ ਸ਼੍ਰੇਣੀਆਂ ਸ਼ਾਮਲ'
    },
    
    'Odia': {
        'title': 'ଭାରତୀୟ ସାଂସ୍କୃତିକ ଐତିହ୍ୟ ଅନ୍ୱେଷକ',
        'subtitle': 'ଭାରତର ସମୃଦ୍ଧ ସାଂସ୍କୃତିକ ଐତିହ୍ୟ ଆବିଷ୍କାର କରନ୍ତୁ, ଶିଖନ୍ତୁ ଏବଂ ଯୋଗଦାନ ଦିଅନ୍ତୁ',
        'welcome_title': 'ଆମର ସାଂସ୍କୃତିକ ଯାତ୍ରାକୁ ସ୍ୱାଗତ',
        'welcome_message': 'ଭାରତର ଅବିଶ୍ୱସନୀୟ ସାଂସ୍କୃତିକ ବିବିଧତାକୁ ସଂରକ୍ଷଣ ଏବଂ ଅଂଶୀଦାର କରିବାରେ ଆମ ସହିତ ଯୋଗ ଦିଅନ୍ତୁ। ଆପଣଙ୍କର ଅବଦାନ ଭବିଷ୍ୟତ ପିଢ଼ିମାନଙ୍କ ପାଇଁ ଏକ ବ୍ୟାପକ ଜ୍ଞାନ ଆଧାର ନିର୍ମାଣରେ ସାହାଯ୍ୟ କରେ।',
        'community_title': 'ଏକତ୍ରେ ସାଂସ୍କୃତିକ ସେତୁ ନିର୍ମାଣ',
        'community_message': 'ଆପଣ ଅଂଶୀଦାର କରୁଥିବା ପ୍ରତ୍ୟେକ କାହାଣୀ, ଶବ୍ଦ ଏବଂ ପରମ୍ପରା ଭାରତୀୟ ଐତିହ୍ୟ ବିଷୟରେ ଆମର ସାମୂହିକ ବୁଝାମଣାକୁ ସମୃଦ୍ଧ କରେ। ଏକତ୍ରେ ଆମେ ସାଂସ୍କୃତିକ ଜ୍ଞାନର ଏକ ଜୀବନ୍ତ ଭଣ୍ଡାର ସୃଷ୍ଟି କରୁଛୁ।',
        'data_usage_note': 'ସମସ୍ତ ଅବଦାନ ଶିକ୍ଷାଗତ ଏବଂ ସାଂସ୍କୃତିକ ସଂରକ୍ଷଣ ଉଦ୍ଦେଶ୍ୟରେ ସମ୍ମାନଜନକ ଭାବରେ ବ୍ୟବହୃତ ହୁଏ।',
        'contribute_now': 'ବର୍ତ୍ତମାନ ଅବଦାନ ଦିଅନ୍ତୁ',
        'explore_culture': 'ସଂସ୍କୃତି ଅନ୍ୱେଷଣ କରନ୍ତୁ',
        'your_contributions': 'ଆପଣଙ୍କର ଅବଦାନ',
        'recent_activity': 'ସମ୍ପ୍ରଦାୟର ସାମ୍ପ୍ରତିକ କାର୍ଯ୍ୟକଳାପ',
        'quality_content': 'ଗୁଣବତ୍ତା ସାଂସ୍କୃତିକ ବିଷୟବସ୍ତୁ',
        'diverse_languages': 'ବିବିଧ ଭାଷାର ପ୍ରତିନିଧିତ୍ୱ',
        'cultural_categories': 'ସାଂସ୍କୃତିକ ବର୍ଗଗୁଡ଼ିକ ଅନ୍ତର୍ଭୁକ୍ତ'
    }
}

def get_translations(language: str) -> dict:
    """
    Get translations for a specific language.
    
    Args:
        language: The language to get translations for
    
    Returns:
        dict: Translation dictionary for the specified language
    """
    
    # Handle language variants - extract the language code
    language_map = {
        'English': 'English',
        'हिन्दी (Hindi)': 'Hindi',
        'বাংলা (Bengali)': 'Bengali', 
        'தமிழ் (Tamil)': 'Tamil',
        'తెలుగు (Telugu)': 'Telugu',
        'मराठी (Marathi)': 'Marathi',
        'ગુજરાતી (Gujarati)': 'Gujarati',
        'ಕನ್ನಡ (Kannada)': 'Kannada',
        'മലയാളം (Malayalam)': 'Malayalam',
        'ਪੰਜਾਬੀ (Punjabi)': 'Punjabi',
        'ଓଡିଆ (Odia)': 'Odia'
    }
    
    # Get the mapped language or use the input as-is
    mapped_language = language_map.get(language, language)
    
    # Return translations or fallback to English
    return TRANSLATIONS.get(mapped_language, TRANSLATIONS['English'])

def get_language_native_name(language_key: str) -> str:
    """
    Get the native name for a language.
    
    Args:
        language_key: The language key from SUPPORTED_LANGUAGES
    
    Returns:
        str: Native name of the language
    """
    return language_key

def get_language_code(language_display: str) -> str:
    """
    Get the language code from display name.
    
    Args:
        language_display: Display name of the language
    
    Returns:
        str: Language code
    """
    language_map = {
        'English': 'en',
        'हिन्दी (Hindi)': 'hi',
        'বাংলা (Bengali)': 'bn',
        'தமிழ் (Tamil)': 'ta',
        'తెలుగు (Telugu)': 'te',
        'मराठी (Marathi)': 'mr',
        'ગુજરાતી (Gujarati)': 'gu',
        'ಕನ್ನಡ (Kannada)': 'kn',
        'മലയാളം (Malayalam)': 'ml',
        'ਪੰਜਾਬੀ (Punjabi)': 'pa',
        'ଓଡିଆ (Odia)': 'or'
    }
    
    return language_map.get(language_display, 'en')

def get_cultural_terms_translation(term: str, target_language: str) -> str:
    """
    Get translation for specific cultural terms.
    
    Args:
        term: The cultural term to translate
        target_language: Target language for translation
    
    Returns:
        str: Translated term or original if translation not available
    """
    
    cultural_terms = {
        'dharma': {
            'Hindi': 'धर्म',
            'Bengali': 'ধর্ম',
            'Tamil': 'தர்மம்',
            'Telugu': 'ధర్మం',
            'Marathi': 'धर्म',
            'Gujarati': 'ધર્મ',
            'Kannada': 'ಧರ್ಮ',
            'Malayalam': 'ധർമ്മം',
            'Punjabi': 'ਧਰਮ',
            'Odia': 'ଧର୍ମ'
        },
        'karma': {
            'Hindi': 'कर्म',
            'Bengali': 'কর্ম',
            'Tamil': 'கர்மா',
            'Telugu': 'కర్మ',
            'Marathi': 'कर्म',
            'Gujarati': 'કર્મ',
            'Kannada': 'ಕರ್ಮ',
            'Malayalam': 'കർമ്മം',
            'Punjabi': 'ਕਰਮ',
            'Odia': 'କର୍ମ'
        },
        'moksha': {
            'Hindi': 'मोक्ष',
            'Bengali': 'মোক্ষ',
            'Tamil': 'மோக்ஷம்',
            'Telugu': 'మోక్షం',
            'Marathi': 'मोक्ष',
            'Gujarati': 'મોક્ષ',
            'Kannada': 'ಮೋಕ್ಷ',
            'Malayalam': 'മോക്ഷം',
            'Punjabi': 'ਮੋਖ',
            'Odia': 'ମୋକ୍ଷ'
        },
        'yoga': {
            'Hindi': 'योग',
            'Bengali': 'যোগ',
            'Tamil': 'யோகா',
            'Telugu': 'యోగ',
            'Marathi': 'योग',
            'Gujarati': 'યોગ',
            'Kannada': 'ಯೋಗ',
            'Malayalam': 'യോഗം',
            'Punjabi': 'ਯੋਗ',
            'Odia': 'ଯୋଗ'
        },
        'guru': {
            'Hindi': 'गुरु',
            'Bengali': 'গুরু',
            'Tamil': 'குரு',
            'Telugu': 'గురు',
            'Marathi': 'गुरु',
            'Gujarati': 'ગુરુ',
            'Kannada': 'ಗುರು',
            'Malayalam': 'ഗുരു',
            'Punjabi': 'ਗੁਰੂ',
            'Odia': 'ଗୁରୁ'
        }
    }
    
    if term.lower() in cultural_terms:
        return cultural_terms[term.lower()].get(target_language, term)
    
    return term

def validate_language_support(language: str) -> bool:
    """
    Check if a language is supported by the translation system.
    
    Args:
        language: Language to check
    
    Returns:
        bool: True if supported, False otherwise
    """
    return language in SUPPORTED_LANGUAGES or language in TRANSLATIONS

def get_available_languages() -> list:
    """
    Get list of all available languages.
    
    Returns:
        list: List of supported language names
    """
    return list(SUPPORTED_LANGUAGES.keys())

def get_translation_completeness() -> dict:
    """
    Get completeness statistics for translations.
    
    Returns:
        dict: Statistics about translation coverage
    """
    base_keys = set(TRANSLATIONS['English'].keys())
    completeness = {}
    
    for lang, translations in TRANSLATIONS.items():
        translated_keys = set(translations.keys())
        completeness[lang] = {
            'total_keys': len(base_keys),
            'translated_keys': len(translated_keys),
            'completion_rate': len(translated_keys) / len(base_keys) * 100,
            'missing_keys': base_keys - translated_keys
        }
    
    return completeness

