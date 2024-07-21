def vowels_and_consonant(input_string):

	user_input = input("Enter a string: ")
	
	consonants = [b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z, A, B, C, D, E, F, G, H, J, K, L, M, N , P, Q, R, S, T, V, W, X, Y, Z]
	vowels = [aeiouAEIOU]

	vowel_count = 0
	consonant_count =0

	for char in user_input:
		if char.isalpha():

			if char in vowels:
				vowel_count += 1
			elif char in consonants:
				consonant_count += 1

print(f"The input string contains {vowel_count} vowels and {consonant_count} consonants.")


