'''

By: Phant0m The Great

'''

import os, carreg, c, time, banners

try: 

 carreg.carreg()

 while True:

  os.system('clear')

  print(banners.banner1)

  print(f'''

┎――――――――――――――――――――――――――――――――――――――――┒

|                 {c.yellow}MENU{c.white}                   |

|――――――――――――――――――――――――――――――――――――――――|

| [01] {c.red}Dorking link{c.white} │ [03] {c.red}Criador{c.white}       |

| [02] {c.red}Informações{c.white}  │ [00] {c.red}Sair{c.white}          |

└――――――――――――――――――――――――――――――――――――――――┘

''')

  ech=input(f'[{c.cyan}?{c.white}] Digite a sua escolha: ')

  if ech=='01' or ech=='1':

    os.system('clear')

    print(banners.banner1)

    print(f'\n[{c.yellow}${c.white}] Digite a classificação do Dorking.\n\n[{c.red}01{c.white}] Dorkings Personalizada\n\n[{c.red}02{c.white}] Dorkinhs Prontas')

    a=input(f'\n{c.bcyan}>{c.white}')

    if a == '01' or a == '1':

     os.system('clear')

     print(banners.banner1)

     while True:

      rep=input(f'\n[{c.cyan}?{c.white}] Digite o parâmetro de busca ↓\n\n{c.bcyan}>{c.white}')

      if rep=='':

        continue

      else:

        break

     rep=rep.replace(" ", "+")

     os.system('clear')

     print(banners.banner1)

     print(f'''\n[{c.yellow}${c.white}] Digite o modelo do Dorking.

   

[{c.red}01{c.white}] Nome de usuário/número

[{c.red}02{c.white}] Site''')

     typpe=input(f'\n{c.cyan}>{c.white}')

     if typpe=='01' or typpe=='1':

       os.system('clear')

       print(banners.banner1)

       print(f'{c.cyan}Carregando links...{c.white}')

       time.sleep(1.5)

       os.system('clear')

       print(banners.banner1)

       print(f'''

     \n

{c.bblue}(DORKINGS GERAIS ↓)\n\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:txt\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:csv\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:pdf\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:doc\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:docx\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:log\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:json\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:xml\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:xls\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:xlsx\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:odt\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:html\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:php\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:asp\n\n{c.bblue}(DORKINGS DE IMAGENS ↓)\n\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})&hl=&tbm=isch&source=hp&biw=&bih=&sclient=img\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:png&hl=&tbm=isch&source=hp&biw=&bih=&sclient=img\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:jpg&hl=&tbm=isch&source=hp&biw=&bih=&sclient=img\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:jpeg&hl=&tbm=isch&source=hp&biw=&bih=&sclient=img\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:gif&hl=&tbm=isch&source=hp&biw=&bih=&sclient=img\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:raw&hl=&tbm=isch&source=hp&biw=&bih=&sclient=img\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:ico&hl=&tbm=isch&source=hp&biw=&bih=&sclient=img\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:bmp&hl=&tbm=isch&source=hp&biw=&bih=&sclient=img\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:svg&hl=&tbm=isch&source=hp&biw=&bih=&sclient=img\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:webp&hl=&tbm=isch&source=hp&biw=&bih=&sclient=img\n\n{c.bblue}(DORKINGS DE VÍDEOS/ÁUDIOS ↓)\n\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})&hl=&tbm=vid&ei=sclient=gws-wiz-video\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:www.youtube.com+intext:({rep})&hl=&tbm=vid&ei=sclient=gws-wiz-video\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:www.tiktok.com+intext:({rep})&hl=&tbm=vid&ei=sclient=gws-wiz-video\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:www.facebook.com+intext:({rep})&hl=&tbm=vid&ei=sclient=gws-wiz-video\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:www.twitter.com+intext:(oaoa)&hl=&tbm=vid&ei=sclient=gws-wiz-video\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:www.twitch.tv+intext:({rep})&hl=&tbm=vid&ei=sclient=gws-wiz-video\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:www.instagram.com+intext:({rep})&hl=&tbm=vid&ei=sclient=gws-wiz-video\n\n{c.bblue}(DORKINGS DE EMAIL ↓)\n\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:txt\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:csv\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:pdf\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:doc\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:docx\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:log\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:json\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:xml\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:xls\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:xlsx\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Email+OR+E-mail+OR+email+OR+e-mail)+filetype:odt\n\n{c.bblue}(DORKINGS DE SENHAS ↓)\n\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:txt\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:csv\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:pdf\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:doc\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:docx\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:log\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:json\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:xml\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:xls\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:xlsx\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:{rep}(Password+OR+password+OR+PASSWORD)+filetype:odt\n\n{c.bblue}(DORKINGS DE TÍTULOS ↓)\n\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:txt\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:csv\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:pdf\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:doc\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:docx\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:log\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:json\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:xml\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:xls\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:xlsx\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:odt\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:html\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:php\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intitle:({rep})+filetype:asp''')

       input(f'\n{c.byellow}(ENTER){c.white} para voltar ao menu.')

     elif typpe=='02' or typpe=='2':

       os.system('clear')

       print(banners.banner1)

       print(f'{c.cyan}Carregando links...{c.white}')

       time.sleep(1.5)

       os.system('clear')

       print(banners.banner1)

       print(f'''

     \n

{c.bblue}(DORKINGS SITE ↓)\n\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:txt\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:pdf\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:({rep})+filetype:pdf\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:log\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:doc\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:docx\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:sqlite\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:yaml\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:json\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:xls\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:xlsx\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:csv\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+filetype:md\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+intext:admin+OR+Admin\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep}%29+intext:emails+OR+Emails+OR+EMAILS\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=site:(www.{rep})%29+intitle:admin+OR+Admin\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=intext:(www.{rep}+OR+{rep})\n{c.bcyan}[M]{c.white} https://www.google.com/search?q=inurl:(www.{rep}+OR+{rep})''')

       input(f'\n{c.byellow}(ENTER){c.white} para voltar ao menu.')

    elif a == '02' or a == '2':

      os.system('clear')

      print(banners.banner1)

      print(f'\n[ {c.blue}i {c.white}] Dorking para encontrar a vulnerabilidade de Directory Listing em um site ↓\n\n{c.bgreen}[M]{c.white} site:www.siteexemplo.com.br intitle:index.of\n\n[ {c.blue}i {c.white}] Dorking para coletar informações de banco de dados ↓\n\n{c.bgreen}[M]{c.white} filetype:env intext:DB_PASSWORD | intext:AWS_SECRET_ACCESS_KEY | intext:API_SECRET | intext:MAIL_PASSWORD\n\n[ {c.blue}i {c.white}] Dorking para coletar senhas ↓\n\n{c.bgreen}[M]{c.white} filetype:txt "senha" intext:@gmail.com | @hotmail.com | @yahoo.com\n\n[{c.blue} i {c.white}] Dorking para encontrar documentos CPF e RG ↓\n\n{c.bgreen}[M]{c.white} filetype:txt | filetype:pdf | filetype:doc | filetype:docx intext:"CPF" AND intext:"RG" numrange:00000000000-99999999999\n\n[{c.blue} i {c.white}] Dorking para encontrar câmeras de segurança ↓\n\n{c.bgreen}[M]{c.white} intitle:"intelbras" "All Rights Reserved" -.com -.info -.net -.com.br -.org -.ls -.in\n{c.bgreen}[M]{c.white} Camera Live Image inurl:guestimage.html\n\n[{c.blue} i {c.white}] Dorking para encontrar emails vazados ↓\n\n{c.bgreen}[M]{c.white} @ +yahoo +hotmail +gmail filetype:txt\n\n[{c.blue} i {c.white}] Dorking para procurar páginas de roteadores (login) ↓\n\n{c.bgreen}[M]{c.white} intitle:"router" inurl:"home.asp"')

      input(f'\n{c.byellow}(ENTER){c.white} para voltar ao menu.')

      

  elif ech=='02' or ech=='2':

    os.system('clear')

    print(banners.banner1)

    print(f'\n{c.green}[ {c.white}i{c.green} ]{c.white} Sobre: O {c.bwhite}MyObservations{c.white}, foi criado com a intensão de facilitar a criação de links dorkings, deixando mais rápido o uso da técnica "Google Dorking"/"Google Hacking", fazendo links de forma rápida.\n\n{c.green}[ {c.white}i{c.green} ]{c.white} Versão: 2.0\n\n{c.bred}[ {c.white}*{c.bred} ]{c.white} Sobre Falhas/Erros: No sistema do {c.bwhite}MyObservations{c.white} podem ocorrer erros, portanto, caso ache uma tela de erro no sistema, reporte ela entrando em contato com o Criador do {c.bwhite}MyObservations{c.white}.\n')

    input(f'{c.byellow}(ENTER){c.white} para voltar ao menu.')

  elif ech=='03' or ech=='3':

    os.system('clear')

    os.system(f'termux-open-url https://www.phant0m007.repl.co/')

    print(banners.banner1)

    print(f'\n[{c.cyan} C {c.white}] CRIADOR ↓\nPhant0m The Great\n\n[{c.cyan} C {c.white}] CONTA DISCORD ↓\n𝐏𝐡𝐚𝐧𝐭𝟎𝐦 𝐓𝐡𝐞 𝐆𝐫𝐞𝐚𝐭#1150')

    input(f'\n{c.byellow}(ENTER){c.white} para voltar ao menu.')

  elif ech=='00' or ech=='0':

    os.system('clear')

    print(banners.banner1)

    print(f'\n[{c.red}#{c.white}] Volte sempre.')

    exit()

except KeyboardInterrupt:

  os.system('clear')

  print(banners.banner1)

  print(f'\n[{c.red}#{c.white}] Volte sempre.')

  exit()
