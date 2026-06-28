# [Ultimate Find-and-Replace Game! 🎮](https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150)

**Can you magically morph string s into string t by completely swapping out its characters?**

To win the game and prove the strings are "isomorphic" (perfect structural twins), your find-and-replace moves must follow two unbreakable rules:

**Rule 1: The Rule of Consistency 🔄** 

If you decide to swap the letter **`'e'`** for the letter **`'a'`**, then every single **`'e'`** in that word must become an **`'a'`**. You can't replace it with **`'a'`** the first time it shows up, and then switch it to **`'o'`** the next time. Once a letter picks its replacement, it has to stick with it!

**Rule 2: The Rule of Exclusivity 🚫**

No two different letters in your starting word can morph into the same letter in the target word. For example, if you replace **`'x'`** with **`'z'`**, you are absolutely not allowed to also replace **`'y'`** with **`'z'`**. Every replacement must be unique. *(Note: A letter is allowed to just map to itself, like replacing 'a' with 'a')*.

### 🎬 Let's see the rules in action!

- #### Example 1: `s = "egg"`, `t = "add"
    > - You replace **`'e'`** with **`'a'`**.
    > - You replace **`'g'`** with **`'d'`**.
    > - The word **`"egg"`** successfully morphs into **`"add"`**! Both rules were followed perfectly.
    > - **Result: True! ✅**

- #### Example 2: `s = "f11"`, `t = "b23"`
    > - You replace **`'f'`** with **`'b'`**.
    > - You replace the first **`'1'`** with **`'2'`**.
    > - Now, the next **`'1'`** comes along... but to make the target word **`"b23"`**, you would have to replace it with **`'3'`**!
    > - Bzzzt! 🚨 You just broke **Rule 1**. You can't replace **`'1'`** with **`'2'`** and then suddenly change your mind and replace it with **`'3'`**.
    > - **Result: False! ❌**

- #### Example 3: `s = "paper"`, `t = "title"`
    > - **`'p'`** becomes **`'t'`**
    > - **`'a'`** becomes **`'i'`**
    > - **`'p'`** becomes **`'t'`** again (*Consistent! Rule 1 is happy)*
    > - **`'e'`** becomes **`'l'`**
    > - **`'r'`** becomes **`'e'`**
    > - Every letter consistently changed to an exclusive target.
    > - **Result: True! ✅** That is the entire scope of the question—just checking if the words can perfectly morph into one another without breaking those two rules!

### Arena Rules (Constraints) 🏟️
- **The Size Limit (`1 <= s.length <= 5 * 10^4`):** You won't be dealing with any empty strings. Your starting word will have at least 1 character, and could be a massive block of text up to 50,000 characters long!

- **The Fair Fight (`t.length == s.length`):** You don't have to worry about mismatched lengths. The starting word and the target word will always have the exact same number of characters.

- **The Character Roster (`s and t consist of any valid ascii character`):** The game isn't just restricted to the standard alphabet! The words can contain numbers, uppercase letters, punctuation marks, spaces, and special symbols (like **`@`** or **`$`**). Any valid ASCII character can be a part of the disguise!
---

### 🧠 The "Double Bouncer" Approach

Think of your algorithm as having two strict bouncers checking IDs at the door using two separate lists (Hash Maps):

1. **The `S-to-T` Bouncer:** Makes sure a letter from **`s`** isn't trying to map to two different letters in **`t`**. (e.g., prevents **`'1'`** from mapping to both **`'2'`** and **`'3'`**).

2. **The `T-to-S` Bouncer:** Makes sure a letter in **`t`** hasn't already been claimed by a different letter from **`s`**. (e.g., prevents both **`'a'`** and **`'d'`** from trying to map to **`'b'`**).

#### The Strategy:

1. **The Quick Reject:** If the strings are different lengths, kick them out immediately. They can't be twins.

2. **The Loop:** Walk through both strings at the exact same time, letter by letter.

3. **The Check:** * If we've seen the **`s`** letter before, check our list: *Is it trying to map to the same **`t`** letter as last time?* If not, reject! ❌

    - If we've seen the **`t`** letter before, check our list: *Is it trying to pair with the same s letter as last time?* If not, reject! ❌

4. **The Handshake:** If both letters are brand new, add them to both bouncers' lists. 🤝

5. **The Success:** If you make it through the whole word without any alarms going off, the strings are isomorphic! 🎉

#### 💻 The Pseudocode
```
FUNCTION isIsomorphic(string_s, string_t):
    
    // 📏 Rule 1: Lengths must match
    IF length of string_s IS NOT EQUAL TO length of string_t:
        RETURN False

    // 🗺️ Create our two bouncer lists (Hash Maps)
    CREATE MAP map_s_to_t
    CREATE MAP map_t_to_s

    // 🚶‍♂️ Walk through both strings index by index
    FOR index FROM 0 TO length of string_s - 1:
        
        char_s = string_s[index]
        char_t = string_t[index]

        // 🚨 Check Bouncer 1: Has char_s been mapped before?
        IF char_s EXISTS IN map_s_to_t:
            // Is it trying to map to a different character now?
            IF map_s_to_t[char_s] IS NOT EQUAL TO char_t:
                RETURN False 

        // 🚨 Check Bouncer 2: Has char_t been claimed before?
        IF char_t EXISTS IN map_t_to_s:
            // Is it claimed by a different character?
            IF map_t_to_s[char_t] IS NOT EQUAL TO char_s:
                RETURN False 

        // ✨ Brand new pair! Register them in both maps
        IF char_s DOES NOT EXIST IN map_s_to_t AND char_t DOES NOT EXIST IN map_t_to_s:
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s

    // 🎉 We checked every letter and broke no rules!
    RETURN True
```

#### ⏱️ Complexity Analysis
- **⏳ Time Complexity: `O(N)` —** We only iterate through the strings a single time, and dictionary lookups run in ultra-fast **`O(1)`** time. ⚡

- **💾 Space Complexity: `O(1)` —** Wait, constant space? Yes! Because the problem guarantees the strings only consist of valid ASCII characters, our dictionaries will hold an absolute maximum of 256 key-value pairs. Since there is a hard upper limit, the space complexity is **`O(1)`** 🧠.
---