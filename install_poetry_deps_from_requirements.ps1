
# python -m pip install pipx
# pipx install poetry
# poetry init

Get-Content requirements.txt | ForEach-Object { poetry add $_ }
