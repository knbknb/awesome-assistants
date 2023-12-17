# Emoji strings to Emoji Chars with Perl
perl -C -pi -E 's/\\u([0-9a-fA-F]{4})/chr(hex($1))/ge'      assistants_joined.yaml 
perl -C -pi -E 's/\\U000([0-9a-fA-F]{4,5})/chr(hex($1))/ge' assistants_joined.yaml