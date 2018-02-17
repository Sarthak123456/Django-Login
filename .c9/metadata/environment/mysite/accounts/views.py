{"changed":true,"filter":false,"title":"views.py","tooltip":"/mysite/accounts/views.py","value":"# -*- coding: utf-8 -*-\nfrom __future__ import unicode_literals\nfrom django.contrib.auth import (\n    authenticate,\n    login,\n    logout,\n    get_user_model,\n    )\nfrom django.shortcuts import render,redirect\nfrom django.http import HttpResponseRedirect\nfrom .forms import UserLoginForm,UserRegisterForm\n\n# Create your views here.\n\ndef login_view(request):\n    print (request.user.is_authenticated())\n    title=\"Login\"\n    form=UserLoginForm(request.POST or None)\n    if form.is_valid():\n        username=form.cleaned_data.get('username')\n        password=form.cleaned_data.get('password')\n        user=authenticate(username=username, password=password)\n        login(request,user)\n        print (request.user.is_authenticated())\n        return redirect(\"/\")\n        \n    return render(request, \"form.html\", {\"form\": form, \"title\" : title})\n\ndef register_view(request):\n    title=\"Register\"\n    form=UserRegisterForm(request.POST or None)\n    if form.is_valid():\n        user=form.save(commit=False)\n        password=form.cleaned_data.get(\"password\")\n        user.set_password(password)\n        user.save()\n        new_user = authenticate(username=user.username, password=password)\n        login(request, new_user)\n        return redirect(\"/login\")\n        \n    context = {\n        \"form\": form,\n        'title': title\n    }\n    return render(request, \"form.html\", context)\n    \ndef logout_view(request):\n    logout(request)\n    return redirect(\"/login\")\n    \ndef index(request):\n    if (request.user.is_authenticated()== True):\n        return render(request, \"index.html\")\n    else:\n        return redirect(\"/login\")\n    \n\n","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":51,"column":33},"end":{"row":51,"column":34},"action":"insert","lines":["i"],"id":824}],[{"start":{"row":51,"column":34},"end":{"row":51,"column":35},"action":"insert","lines":["n"],"id":825}],[{"start":{"row":51,"column":35},"end":{"row":51,"column":36},"action":"insert","lines":["d"],"id":826}],[{"start":{"row":51,"column":36},"end":{"row":51,"column":37},"action":"insert","lines":["e"],"id":827}],[{"start":{"row":51,"column":37},"end":{"row":51,"column":38},"action":"insert","lines":["x"],"id":828}],[{"start":{"row":51,"column":38},"end":{"row":51,"column":39},"action":"insert","lines":["."],"id":829}],[{"start":{"row":51,"column":39},"end":{"row":51,"column":40},"action":"insert","lines":["h"],"id":830}],[{"start":{"row":51,"column":40},"end":{"row":51,"column":41},"action":"insert","lines":["t"],"id":831}],[{"start":{"row":51,"column":41},"end":{"row":51,"column":42},"action":"insert","lines":["m"],"id":832}],[{"start":{"row":51,"column":42},"end":{"row":51,"column":43},"action":"insert","lines":["l"],"id":833}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":45},"action":"remove","lines":["return HttpResponseRedirect('index.html')"],"id":834},{"start":{"row":51,"column":4},"end":{"row":55,"column":48},"action":"insert","lines":["context = {","        \"form\": form,","        'title': title","    }","    return render(request, \"form.html\", context)"]}],[{"start":{"row":52,"column":8},"end":{"row":52,"column":21},"action":"remove","lines":["\"form\": form,"],"id":835}],[{"start":{"row":52,"column":8},"end":{"row":53,"column":0},"action":"remove","lines":["",""],"id":836}],[{"start":{"row":52,"column":8},"end":{"row":52,"column":12},"action":"remove","lines":["    "],"id":837}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"remove","lines":["    "],"id":838}],[{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"insert","lines":["    "],"id":839}],[{"start":{"row":53,"column":4},"end":{"row":53,"column":8},"action":"insert","lines":["    "],"id":840}],[{"start":{"row":50,"column":19},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":841},{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":5},"action":"insert","lines":["t"],"id":842}],[{"start":{"row":51,"column":5},"end":{"row":51,"column":6},"action":"insert","lines":["i"],"id":843}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":6},"action":"remove","lines":["ti"],"id":844},{"start":{"row":51,"column":4},"end":{"row":51,"column":9},"action":"insert","lines":["title"]}],[{"start":{"row":51,"column":9},"end":{"row":51,"column":10},"action":"insert","lines":[" "],"id":845}],[{"start":{"row":51,"column":10},"end":{"row":51,"column":11},"action":"insert","lines":["="],"id":846}],[{"start":{"row":51,"column":11},"end":{"row":51,"column":12},"action":"insert","lines":[" "],"id":847}],[{"start":{"row":51,"column":12},"end":{"row":51,"column":14},"action":"insert","lines":["\"\""],"id":848}],[{"start":{"row":51,"column":13},"end":{"row":51,"column":14},"action":"insert","lines":["I"],"id":849}],[{"start":{"row":51,"column":14},"end":{"row":51,"column":15},"action":"insert","lines":["n"],"id":850}],[{"start":{"row":51,"column":15},"end":{"row":51,"column":16},"action":"insert","lines":["d"],"id":851}],[{"start":{"row":51,"column":16},"end":{"row":51,"column":17},"action":"insert","lines":["e"],"id":852}],[{"start":{"row":51,"column":16},"end":{"row":51,"column":17},"action":"remove","lines":["e"],"id":853}],[{"start":{"row":51,"column":15},"end":{"row":51,"column":16},"action":"remove","lines":["d"],"id":854}],[{"start":{"row":51,"column":14},"end":{"row":51,"column":15},"action":"remove","lines":["n"],"id":855}],[{"start":{"row":51,"column":13},"end":{"row":51,"column":14},"action":"remove","lines":["I"],"id":856}],[{"start":{"row":51,"column":13},"end":{"row":51,"column":14},"action":"insert","lines":["i"],"id":857}],[{"start":{"row":51,"column":14},"end":{"row":51,"column":15},"action":"insert","lines":["n"],"id":858}],[{"start":{"row":51,"column":15},"end":{"row":51,"column":16},"action":"insert","lines":["d"],"id":859}],[{"start":{"row":55,"column":28},"end":{"row":55,"column":32},"action":"remove","lines":["form"],"id":959},{"start":{"row":55,"column":28},"end":{"row":55,"column":29},"action":"insert","lines":["i"]}],[{"start":{"row":55,"column":29},"end":{"row":55,"column":30},"action":"insert","lines":["n"],"id":960}],[{"start":{"row":55,"column":30},"end":{"row":55,"column":31},"action":"insert","lines":["d"],"id":961}],[{"start":{"row":55,"column":31},"end":{"row":55,"column":32},"action":"insert","lines":["e"],"id":962}],[{"start":{"row":55,"column":32},"end":{"row":55,"column":33},"action":"insert","lines":["x"],"id":963}],[{"start":{"row":48,"column":22},"end":{"row":48,"column":23},"action":"insert","lines":["l"],"id":964}],[{"start":{"row":48,"column":23},"end":{"row":48,"column":24},"action":"insert","lines":["o"],"id":965}],[{"start":{"row":48,"column":24},"end":{"row":48,"column":25},"action":"insert","lines":["g"],"id":966}],[{"start":{"row":48,"column":25},"end":{"row":48,"column":26},"action":"insert","lines":["i"],"id":967}],[{"start":{"row":48,"column":26},"end":{"row":48,"column":27},"action":"insert","lines":["n"],"id":968}],[{"start":{"row":51,"column":4},"end":{"row":54,"column":9},"action":"remove","lines":["title = \"ind\"","    context = {","            'title': title","        }"],"id":969}],[{"start":{"row":51,"column":4},"end":{"row":52,"column":0},"action":"remove","lines":["",""],"id":970}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":8},"action":"remove","lines":["    "],"id":971}],[{"start":{"row":51,"column":41},"end":{"row":51,"column":48},"action":"remove","lines":["context"],"id":972}],[{"start":{"row":51,"column":40},"end":{"row":51,"column":41},"action":"remove","lines":[" "],"id":973}],[{"start":{"row":51,"column":39},"end":{"row":51,"column":40},"action":"remove","lines":[","],"id":974}],[{"start":{"row":50,"column":19},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":976},{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":5},"action":"insert","lines":["i"],"id":977}],[{"start":{"row":51,"column":5},"end":{"row":51,"column":6},"action":"insert","lines":["f"],"id":978}],[{"start":{"row":51,"column":6},"end":{"row":51,"column":7},"action":"insert","lines":[" "],"id":979}],[{"start":{"row":51,"column":7},"end":{"row":51,"column":38},"action":"insert","lines":["request.user.is_authenticated()"],"id":980}],[{"start":{"row":51,"column":38},"end":{"row":51,"column":39},"action":"insert","lines":["="],"id":981}],[{"start":{"row":51,"column":39},"end":{"row":51,"column":40},"action":"insert","lines":["="],"id":982}],[{"start":{"row":51,"column":40},"end":{"row":51,"column":41},"action":"insert","lines":[" "],"id":983}],[{"start":{"row":51,"column":41},"end":{"row":51,"column":42},"action":"insert","lines":["T"],"id":984}],[{"start":{"row":51,"column":42},"end":{"row":51,"column":43},"action":"insert","lines":["r"],"id":985}],[{"start":{"row":51,"column":43},"end":{"row":51,"column":44},"action":"insert","lines":["u"],"id":986}],[{"start":{"row":51,"column":44},"end":{"row":51,"column":45},"action":"insert","lines":["e"],"id":987}],[{"start":{"row":51,"column":45},"end":{"row":51,"column":46},"action":"insert","lines":[")"],"id":988}],[{"start":{"row":51,"column":46},"end":{"row":51,"column":47},"action":"insert","lines":[":"],"id":989}],[{"start":{"row":51,"column":7},"end":{"row":51,"column":8},"action":"insert","lines":["("],"id":990}],[{"start":{"row":52,"column":4},"end":{"row":52,"column":8},"action":"insert","lines":["    "],"id":991}],[{"start":{"row":52,"column":44},"end":{"row":53,"column":0},"action":"insert","lines":["",""],"id":992},{"start":{"row":53,"column":0},"end":{"row":53,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":53,"column":4},"end":{"row":53,"column":8},"action":"remove","lines":["    "],"id":993}],[{"start":{"row":53,"column":4},"end":{"row":53,"column":5},"action":"insert","lines":["e"],"id":994}],[{"start":{"row":53,"column":5},"end":{"row":53,"column":6},"action":"insert","lines":["l"],"id":995}],[{"start":{"row":53,"column":6},"end":{"row":53,"column":7},"action":"insert","lines":["s"],"id":996}],[{"start":{"row":53,"column":7},"end":{"row":53,"column":8},"action":"insert","lines":["e"],"id":997}],[{"start":{"row":53,"column":8},"end":{"row":53,"column":9},"action":"insert","lines":[":"],"id":998}],[{"start":{"row":53,"column":9},"end":{"row":54,"column":0},"action":"insert","lines":["",""],"id":999},{"start":{"row":54,"column":0},"end":{"row":54,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":54,"column":8},"end":{"row":54,"column":9},"action":"insert","lines":["r"],"id":1000}],[{"start":{"row":54,"column":9},"end":{"row":54,"column":10},"action":"insert","lines":["e"],"id":1001}],[{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"insert","lines":["t"],"id":1002}],[{"start":{"row":54,"column":11},"end":{"row":54,"column":12},"action":"insert","lines":["u"],"id":1003}],[{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"insert","lines":["r"],"id":1004}],[{"start":{"row":54,"column":13},"end":{"row":54,"column":14},"action":"insert","lines":["n"],"id":1005}],[{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"insert","lines":[" "],"id":1006}],[{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"insert","lines":["r"],"id":1007}],[{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"insert","lines":["e"],"id":1008}],[{"start":{"row":54,"column":17},"end":{"row":54,"column":18},"action":"insert","lines":["d"],"id":1009}],[{"start":{"row":54,"column":18},"end":{"row":54,"column":19},"action":"insert","lines":["i"],"id":1010}],[{"start":{"row":54,"column":19},"end":{"row":54,"column":20},"action":"insert","lines":["r"],"id":1011}],[{"start":{"row":54,"column":20},"end":{"row":54,"column":21},"action":"insert","lines":["e"],"id":1012}],[{"start":{"row":54,"column":21},"end":{"row":54,"column":22},"action":"insert","lines":["c"],"id":1013}],[{"start":{"row":54,"column":22},"end":{"row":54,"column":23},"action":"insert","lines":["t"],"id":1014}],[{"start":{"row":54,"column":23},"end":{"row":54,"column":25},"action":"insert","lines":["()"],"id":1015}],[{"start":{"row":54,"column":24},"end":{"row":54,"column":26},"action":"insert","lines":["\"\""],"id":1016}],[{"start":{"row":54,"column":25},"end":{"row":54,"column":26},"action":"insert","lines":["'"],"id":1017}],[{"start":{"row":54,"column":25},"end":{"row":54,"column":26},"action":"remove","lines":["'"],"id":1018}],[{"start":{"row":54,"column":25},"end":{"row":54,"column":26},"action":"insert","lines":["/"],"id":1019}],[{"start":{"row":54,"column":26},"end":{"row":54,"column":27},"action":"insert","lines":["l"],"id":1020}],[{"start":{"row":54,"column":27},"end":{"row":54,"column":28},"action":"insert","lines":["o"],"id":1021}],[{"start":{"row":54,"column":28},"end":{"row":54,"column":29},"action":"insert","lines":["g"],"id":1022}],[{"start":{"row":54,"column":29},"end":{"row":54,"column":30},"action":"insert","lines":["i"],"id":1023}],[{"start":{"row":54,"column":30},"end":{"row":54,"column":31},"action":"insert","lines":["n"],"id":1024}],[{"start":{"row":13,"column":0},"end":{"row":55,"column":4},"action":"remove","lines":["","def login_view(request):","    print (request.user.is_authenticated())","    title=\"Login\"","    form=UserLoginForm(request.POST or None)","    if form.is_valid():","        username=form.cleaned_data.get('username')","        password=form.cleaned_data.get('password')","        user=authenticate(username=username, password=password)","        login(request,user)","        print (request.user.is_authenticated())","        return redirect(\"/\")","        ","    return render(request, \"form.html\", {\"form\": form, \"title\" : title})","","def register_view(request):","    title=\"Register\"","    form=UserRegisterForm(request.POST or None)","    if form.is_valid():","        user=form.save(commit=False)","        password=form.cleaned_data.get(\"password\")","        user.set_password(password)","        user.save()","        new_user = authenticate(username=user.username, password=password)","        login(request, new_user)","        return redirect(\"/login\")","        ","    context = {","        \"form\": form,","        'title': title","    }","    return render(request, \"form.html\", context)","    ","def logout_view(request):","    logout(request)","    return redirect(\"/login\")","    ","def index(request):","    if (request.user.is_authenticated()== True):","        return render(request, \"index.html\")","    else:","        return redirect(\"/login\")","    "],"id":1025},{"start":{"row":13,"column":0},"end":{"row":21,"column":49},"action":"insert","lines":["from django.contrib.auth import (","    authenticate,","    login,","    logout,","    get_user_model,","    )","from django.shortcuts import render,redirect","from django.http import HttpResponseRedirect","from .forms import UserLoginForm,UserRegisterForm"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":0},"end":{"row":10,"column":49},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1514952407374}