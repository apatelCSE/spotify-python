Issues/Journal
==============

- The main use case I'd like to create this for is a Bollywood singer who sings in Hindi, Telugu, Tamil, Kannada, Odia, Nepali, Bhojpuri, Bengali. I'm trying to figure out the best way to search for songs based on the first word of the song. One idea I have is to ask the user for the language they want the playlist to be restricted to (have one playlist for the artist's Tamil songs, one for Hindi songs, etc.). I could then load the language's dictionary and search by each word in the dictionary. This poses a few obvious issues, the most obvious being the sheer volume and extensive search involved with searching every single word in one language. There are also quite a few languages out there, and this implementation would require storing every language's wordset. Another issue that arises with that is the multiple spellings of one word in Romanized text. Perhaps there could be a way to pull that information from a different API.

- Better idea: Traverse through each letter and while there are still songs per that letter by the provided artist, traverse through the alphabet again: A -> Aa -> Aaa -> Aab. This would work for all languages now because everything has to be Romanized for Spotify (would this only work) for USA users? Hmm...). We don't have to store all those languages now. The search time is still exhaustive, however.

- Pseudocode for the recursive search:
    ```cpp
        search(artist)
            for letter in alphabet
                runsearch(letter)
        
        runsearch (artist, letterstring)
            if (search results with letterstring)
                numresults = number of search results
                for songs in search results
                    addsong(song)
                if numresults > limit_of_search_results
                    for letter in alphabet
                        runsearch(artist, letterstring + letter)

        addsong (song)
            if URI already in playlist
                return
            else
                add to playlist
    ```
- One problem I'm running into during the debugging process (good news, I can create playlists!) is that this search is crazy-exhaustive. There are too many results, and not enough with the correct artist, which is weird because the search should be specific to the correct-matching artist and search string. Instead, we're getting to the point where the search string is "aaaaaaaaa" and there are still 50+ results...

- I just learned about the "offset" feature in search, so I could try to offset my searches instead of recursing with the next letter, which should hopefully bring the runtime down.

- The program works, which is so exciting! The tracks are added in a somewhat alphabetical order, and I couldn't be happier. The only issue now is that it appears that "copies" of the same song are added to the playlist. I checked it and it looks like the song names are the same, but the URIs are different (which is great, it means that my program works correctly). I did some research online and the reason is that some songs get re-released on different albums or special playlists (like the "This is" playlist). I'm not sure if I may want to run a cleaning function on the playlist at the end of the program to ensure that the playlist songs are unique.

- I tried running the program on Conan Gray (only 57 songs in the final playlist) and on Taylor Swift (~100 unique songs, I believe). The program filled Conan's playlist successfully and crashed on Taylor's. I had the program print the URIs populated, and it looks like the first part of the program worked correctly for Taylor, but I think there's a limit on how much you can load the JSON request. I'm going to try splitting the requests and doing an offset-type thing.