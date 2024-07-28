from django.shortcuts import render
from django.contrib import messages
import openai

# Create your views here.

def home(request):

    lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'markup', 'markup-templating', 'matlab', 'mongodb', 'objectivec', 'perl', 'php', 'powershell', 'python', 'r', 'regex', 'ruby', 'rust', 'sas', 'sql', 'typescript', 'yaml']
    
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        
        # ensuring lang selected
        if lang == "slct":
            messages.success(request, "Please select a programming language")
            return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
        
        else:
            #openAI keys
            openai.api_key = "Enter_your_api_key"
            
            #openAi instance
            openai.Model.list()
            
            #request
            
            try:
                response = openai.Completion.create(
                    engine = 'tts-1',
                    prompt = f"Please respond only with code, nothing else. Fix this {lang} code. code: {code}",
                    temperature = 0,
                    max_tokens = 1000, #if code is cut off add tokens
                    top_p = 1.0,
                    frequency_penalty = 0.0,
                    presense_penalty = 0.0,
                    )
                 
                #parsing response
                response = (response["choices"][0]["text"]).strip()
                    
                return render(request, 'home.html', {'lang_list': lang_list, 'response': response, 'lang': lang})
            
            except Exception as e: 
                return render(request, 'home.html', {'lang_list': lang_list, 'response': e, 'lang': lang})
    return render(request, 'home.html', {'lang_list': lang_list})
