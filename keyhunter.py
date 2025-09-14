#!/bin/bash/python

import requests
import re
import sys

# Banner ASCII
banner = """
############################################################
# _  _________   __    _   _ _   _ _   _ _____ _____ ____  # 
#| |/ / ____\ \ / /   | | | | | | | \ | |_   _| ____|  _ \ #
#| ' /|  _|  \ V /____| |_| | | | |  \| | | | |  _| | |_) |#
#| . \| |___  | |_____|  _  | |_| | |\  | | | | |___|  _ < #
#|_|\_\_____| |_|     |_| |_|\___/|_| \_| |_| |_____|_| \_\#
#Hunt. Seek. Find           |             Code by nailtpax #
############################################################
"""
print(banner)

def main():

    if len(sys.argv) == 1:
        print ("Uso: python keyhunter.py <url> <wordlist>")
        print("É possível utilizar a wordlist default, basta não informar o segundo parâmetro.")
        return 0

    wordlist = []
    keywords = [
            "api_key", "apikey", "_API_key", "token", "access_token",
            "auth_token", "client_secret", "clientid", "client_id",
            "secret", "authorization", "x-api-key", "bearer",
            "password", "passwd", "pwd", "passphrase",
            "private_key", "privkey", "ssh_key", "rsa_key", "dsa_key",
            "secret_key", "app_key", "consumer_key", "consumer_secret",
            "jwt", "jwt_secret", "oauth_token", "oauth_secret",
            "session_token", "sessionid", "cookie", "auth", "credentials",
            "encryption_key", "enckey", "signing_key", "s3_key",
            "db_password", "database_password", "token_key", "refresh_token",
            "accesskey", "access_key_id", "secret_access_key",
            "vault_token", "private_token", "secret_token",
            "aws_access_key_id", "aws_secret_access_key", "aws_session_token",
            "gcp_api_key", "gcp_client_email", "gcp_private_key",
            "azure_client_id", "azure_client_secret", "azure_tenant_id",
            "heroku_api_key", "slack_token", "discord_token", "telegram_token"
        ]
    if len(sys.argv) > 2:
        try:
            with open(sys.argv[2], 'r') as f:
                wordlist = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Wordlist '{sys.argv[2]}' não encontrada. Usando wordlist padrão.")
            wordlist = keywords
    else:
        print("Usando wordlist padrão.")
        wordlist = keywords

    site = sys.argv[1].strip()

    patterns = {
        "AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
        "AWS Secret Access Key": r"(?<![A-Z0-9])[A-Za-z0-9/+=]{40}(?![A-Z0-9])",
        "JWT Token": r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+",
        "Generic Token": r"[A-Za-z0-9]{32,}"
    }

    def search_keywords(content, source="HTML"):
        found = False
        for word in keywords:
            matches = re.findall(rf"{word}['\"]?\s*[:=]\s*['\"]?([\w-]+)", content, re.IGNORECASE)
            if matches:
                found = True
                print(f"\n[+] PossÃvel '{word}' encontrado no {source}:")
                for m in matches:
                    print(f"    {m}")
        return found

    try:
        r = requests.get(site)
        r.raise_for_status()
    except Exception as e:
        print(f"Erro ao acessar o site: {e}")
        exit()

    html_content = r.text
    search_keywords(html_content, "HTML")

if __name__ == "__main__":
    print("\n[+] Iniciando busca por chaves e tokens...")
    main()
