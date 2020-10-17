try:
    import speedtest
    import time
    import os
except:
   print("Você não tem speedtest-cli!")
   print("Por favor, instale usando > pip install speedtest-cli")
   print("E tente novamente!")
else:
    def medir_velocidade_internet(tudo=False):
        speed=speedtest.Speedtest()
        download=speed.download()
        upload=speed.upload()
        if tudo:
            download_real = str(download)
            upload_real = str(upload)
            print("=="*10)
            print("Download: {}Mbps".format(download_real[0:2]))
            print("Upload:{}Mbps".format(upload_real[0:2]))
            print("=="*10)
            time.sleep(1.3)
    def medir_download(download=False):
        speed=speedtest.Speedtest()
        download=speed.download()                    # By Lucas Silva (lucas-DK)
        upload=speed.upload()
        if download:
            download_real = str(download)
            print("=="*10)
            print("Download: {}Mbps".format(download_real[0:2]))
            print("=="*10)
            time.sleep(1.3)
    def medir_upload(upload=False):
        speed=speedtest.Speedtest()
        download=speed.download()
        upload=speed.upload()
        if upload:
            upload_real = str(upload)
            print("=="*10)
            print("Upload: {}Mbps".format(upload_real[0:2]))
            print("=="*10)
            time.sleep(1.3)
    def limpar_terminal():
        os.system("clear")

    while True:
        print("""
 _____   _____   _____   _____   _____   __   _   _____   _____  
/  ___/ |  _  \ | ____| | ____| |  _  \ |  \ | | | ____| |_   _| 
| |___  | |_| | | |__   | |__   | | | | |   \| | | |__     | |   
\___  \ |  ___/ |  __|  |  __|  | | | | | |\   | |  __|    | |   
__ _| | | |     | |___  | |___  | |_| | | | \  | | |___    | |   
/_____/ |_|     |_____| |_____| |_____/ |_|  \_| |_____|   |_|   


Menu:

[1] - Testar download e upload
[2] - Testar download
[3] - Testar upload
[4] - Limpar terminal
[x] - Sair

        """)

        resp = input(">>>> ")
        if resp.isnumeric():
            resp = int(resp)
            if resp == 1:
                print("Testando velocidade do download e upload...\n")
                medir_velocidade_internet(tudo=True)
            elif resp == 2:
                print("Testando velocidade do download...\n")
                medir_download(download=True)
            elif resp == 3:
                print("Testando velocidade do upload...\n")
                medir_upload(upload=True)
            elif resp == 4:
                limpar_terminal()
            elif resp < 1 or resp > 4:
                print('\nOpção inválida!')
                print('Tente novamente!\n')

        elif resp.isalpha():
            if resp in 'X' or resp in 'x':
                print("Saindo...")
                time.sleep(1)
                break
            else:
                print('Opção inválida!')
