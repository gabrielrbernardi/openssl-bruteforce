#comparar arquivo de saida do openssl para ver se foi decifrado corretamente

input="pokemonNames1.txt"

while IFS= read -r line
do
	echo "$line" > saida.txt
	openssl enc -d -aes-256-cbc -pbkdf2 -in teste.enc -out saidaDesc.txt -pass pass:"$line"
done < "$input"
