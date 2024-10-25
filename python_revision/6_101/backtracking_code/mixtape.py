import ast

def mixtape(songs: dict, target_duration: int):
    """
    Given a dictionary of songs (mapping titles to durations), as well as a
    total target duration, return a set of song titles such that the sum of
    those songs' durations equals the target_duration.

    If no such set exists, return None instead.

    >>> songs = {'A': 5, 'B': 10, 'C': 6, 'D': 2}
    >>> mixtape(songs, 21) == {'A', 'B', 'C'}
    True
    >>> mixtape(songs, 1000) is None
    True
    >>> mixtape(songs,10)
    {'B'}


    """

    if target_duration == 0:
        return set()
    if not songs:
        return None

    current = list(songs.keys())[0]
    current_duration = songs[current]

    recursive1 = mixtape(
        {k: v for k, v in songs.items() if k != current},
        target_duration - current_duration,
    )

    if recursive1 is not None:
        return {current} | recursive1
    recursive2 = mixtape(
        {key: value for key, value in songs.items() if key != current}, target_duration
    )
    if recursive2 is not None:
        return recursive2
    return None

def mixtape_iterative_backtrack(songs,target_duration):
    if target_duration==0:
        return set()
    if not songs:
        return None
    for key,value in songs.items():
        recursive =  mixtape(
        {k: v for k, v in songs.items() if k!=key},
        target_duration-value,
    )
        if recursive is not None:
            return {key}|recursive
    return None
def mixtape_graph(songs: dict, target_duration: int):

    agenda = {()}
    total_paths = set()
    visited = set()
    count = 0
    while agenda:

        this_path = agenda.pop()

        # this_path=tuple(sorted(this_path))

        count += 1

        # print(type(this_path))

        duration = sum(songs[s] for s in this_path)
        if duration == target_duration:
            return this_path
        if duration > target_duration:
            continue
        for song, duration in songs.items():
            if song not in this_path:
                new_path = tuple(sorted(this_path + (song,)))
                if new_path in visited:
                    continue
                visited.add(new_path)
                agenda.add(new_path)
    print(count)
    # print(visited)
    return None


if __name__ == "__main__":
    # import doctest
    #
    # # print(mixtape())
    # doctest.testmod()  # Working...
    s={
        "Gettin' Jiggy Wit It": 295,
        "Surfin' USA": 774,
        "Fallin'": 241,
        "Time After Time": 929,
        "La Bamba": 368,
        "Set Fire to the Rain": 187,
        "Parallel Universe": 729,
        "London Bridge": 949,
        "High Hopes": 1,
        "The Locomotion": 349,
        "Breathe": 916,
        "Lean on Me": 95,
        "September": 943,
        "All That She Wants": 451,
        "Every Rose Has Its Thorn": 508,
        "Sunshine of Your Love": 27,
        "Tell Her ABout It": 310,
        "A Thousand Miles": 130,
        "Hang on Sloopy": 355,
        "Take Me Home, Country Roads": 198,
        "Ticket to Ride": 189,
        "Always Straight Ahead": 743,
        "Another Brick in the Wall": 111,
        "Word Up!": 263,
        "Problem": 96,
        "Single Ladies (Put a Ring On It)": 161,
        "Upside Down": 121,
        "Waterloo": 449,
        "It's All Right": 517,
        "Kryptonite": 572,
        "At the End of August": 869,
        "Work": 372,
        "I Don't Want to Wait": 188,
        "Safety Dance": 891,
        "Pocket Calculator": 983,
        "Starships": 882,
        "Royals": 605,
        "She Blinded Me With Science": 781,
        "I'm Henry the Eighth, I Am": 492,
        "Don't Dream It's Over": 181,
        "Telephone": 210,
        "Uptown Girl": 99,
        "Groovin'": 558,
        "Rolling in the Deep": 529,
        "Reunited": 477,
        "Turn! Turn! Turn! (To Everything There is a Season)": 73,
        "It's Still Rock and Roll To Me": 229,
        "I Got You, Babe": 65,
        "Burning Heart": 642,
        "22": 420,
        "Summertime": 183,
        "Ring My Bell": 48,
        "Stop! In the Name of Love": 512,
        "Jack & Diane": 705,
        "Boogie Oogie Oogie": 122,
        "Faith": 26,
        "Cat's in the Cradle": 364,
        "Heat Wave": 418,
        "I Want to Hold Your Hand": 804,
        "Wind Beneath My Wings": 971,
        "Livin' on a Prayer": 443,
        "Life Is a Highway": 132,
        "Poker Face": 85,
        "Cold as Ice": 376,
        "Beat It": 12,
        "Glamorous": 54,
        "Bohemian Rhapsody": 432,
        "Blurry": 238,
        "Movies": 614,
        "Bennie and the Jets": 568,
        "Boom Boom Pow": 129,
        "Friday": 64,
        "Radioactive": 426,
        "This Love": 240,
        "Lights": 895,
        "Fancy": 208,
        "Policy of Truth": 154,
        "I Try": 598,
        "Dancing in the Street": 343,
        "Stay": 765,
        "The Wanderer": 465,
        "Dance to the Music": 172,
        "YMCA": 340,
        "Broken Wings": 956,
        "Dancing Machine": 430,
        "The Sweet Escape": 721,
        "Save Tonight": 747,
        "Sandstorm": 831,
        "Hello": 792,
        "I Will Survive": 14,
        "The Twist": 159,
        "Tom's Diner": 872,
        "Smooth": 565,
        "We're an American Band": 566,
        "Paint It, Black": 479,
        "Footloose": 627,
        "Sweet Caroline": 182,
        "My Heart Will Go On": 896,
        "(Sittin' On) The Dock of the Bay": 848,
        "I'm a Believer": 77,
        "Different Summers": 615,
        "Hey Jude": 458,
        "Someday": 662,
        "American Pie": 920,
        "Changes": 501,
        "Umbrella": 569,
        "Nothing Compares 2 U": 963,
        "We Can Work It Out": 546,
        "Genie in a Bottle": 184,
        "Lisztomania": 324,
        "Chariots of Fire": 523,
        "Louie Louie": 483,
        "You're The Best Around": 974,
        "Bette Davis Eyes": 737,
        "Walk Like an Egyptian": 690,
        "A Fifth of Beethoven": 955,
        "Bring Me To Life": 988,
        "Here I Go Again": 265,
        "Roar": 509,
        "How You Remind Me": 990,
        "In My Head": 612,
        "Jump": 498,
        "I Miss You": 524,
        "Hooked on a Feeling": 410,
        "Uptown Funk": 100,
        "San Francisco": 704,
        "Heart of Gold": 914,
        "The Ballroom Blitz": 32,
        "Every Morning": 793,
        "What's Love Got to Do With It": 69,
        "Waterfalls": 808,
        "Tik Tok": 178,
        "Dancing Queen": 237,
        "Rhythm of the Rain": 887,
        "Super Bass": 191,
        "Crazy on You": 836,
        "Behind These Hazel Eyes": 942,
        "Achy Breaky Heart": 706,
        "Fire": 232,
        "Monday, Monday": 819,
        "Love Story": 309,
        "Karma Chameleon": 998,
        "Crazy Little Thing Called Love": 507,
        "California Dreamin'": 370,
        "Straight Up": 234,
        "Hanging by a Moment": 257,
        "Time in a Bottle": 789,
        "The Hustle": 92,
        "Mockingbird": 448,
        "Build Me Up Buttercup": 134,
        "Firework": 298,
        "ABC": 833,
        "Titanium": 592,
        "Billie Jean": 312,
        "Truly Madly Deeply": 68,
        "I Want it That Way": 753,
        "Jump Around": 179,
        "Lady": 38,
        "I Love Rock 'n Roll": 945,
        "C'est La Vie": 33,
        "I Believe I Can Fly": 697,
        "The Distance": 775,
        "Ride": 849,
        "Wrecking Ball": 904,
        "Cars": 39,
        "My Sharona": 858,
        "Miss Independent": 666,
        "Candy Man": 256,
        "Der Kommissar": 357,
        "Jenny from the Block": 979,
        "Hey There Delilah": 652,
        "Jeopardy": 851,
        "Call Me Maybe": 211,
        "Black Horse and the Cherry Tree": 513,
        "Thank You": 862,
        "Mr. Roboto": 333,
        "Bug A Boo": 608,
        "Money for Nothing": 547,
        "Hit 'Em Up Style": 795,
        "Particle Man": 982,
        "Mr. Big Stuff": 365,
        "Let It Be": 647,
        "Macarena": 127,
        "Electric Avenue": 468,
        "Yesterday": 460,
        "Drops of Jupiter": 156,
        "Let's Dance": 617,
        "Love Song": 297,
        "Sugar": 926,
        "Get Ready": 436,
        "Down Under": 2,
        "Celebration": 799,
        "Call Me": 519,
        "Mrs. Brown, You've Got a Lovely Daughter": 337,
        "I'll Be There": 860,
        "Hips Don't Lie": 917,
        "Ghostbusters": 246,
        "Nyan Cat": 94,
        "Sweet Child o' Mine": 428,
        "Respect": 940,
        "Pump Up the Jam": 497,
        "The Way": 661,
        "(I Wear My) Sunglasses at Night": 825,
        "Raindrops Keep Fallin' on My Head": 649,
        "U Can't Touch This": 272,
        "How's It Gonna Be?": 46,
        "That Don't Impress Me Much": 462,
        "It's the Same Old Song": 694,
        "Mony Mony": 149,
        "Magic": 732,
        "Can't Stop the Feeling": 756,
        "Whoomp! (There It Is)": 417,
        "Never Gonna Give You Up": 11,
        "The Sign": 554,
        "Pipeline": 590,
        "Last Train to Clarksville": 714,
        "Watch Me (Whip, Nae Nae)": 838,
        "Fame": 842,
        "Hero": 852,
        "Fergalicious": 786,
        "99 Luftballons": 771,
        "Complicated": 580,
        "Slide": 445,
        "Electric Youth": 381,
        "Express Yourself": 635,
        "Eye of the Tiger": 494,
        "Unwritten": 360,
        "No Scrubs": 577,
        "Just Fance": 220,
        "Swamp Thing": 137,
        "Angel of the Morning": 528,
        "All Around the World (La La La La La)": 49,
        "What Do You Mean?": 1000,
        "Sk8r Boi": 759,
        "Livin' la Vida Loca": 822,
        "Mambo No. 5": 375,
        "Against All Odds (Take a Look At Me Now)": 709,
        "3 AM": 655,
        "Around the World": 209,
        "Spider Snakes": 616,
        "Since U Been Gone": 611,
        "Sugar, Sugar": 883,
        "Hangin' Tough": 457,
        "Do Wah Diddy Diddy": 884,
        "One Step at a Time": 502,
        "Can You Feel the Love Tonight": 194,
        "Hollaback Girl": 863,
        "Blank Space": 680,
        "Hide and Seek": 270,
        "...Baby One More Time": 505,
        "Always Be My Baby": 490,
        "The Great Divide": 411,
        "Picture": 144,
        "Ain't No Mountain High Enough": 878,
        "You've Got a Friend": 300,
        "Shake It Off": 733,
        "Honey": 459,
        "Cheap Thrills": 409,
        "Mrs. Robinson": 168,
        "Heaven is a Place on Earth": 646,
        "I Feel the Earth Move": 293,
        "All for You": 975,
        "Toxic": 292,
        "Sweet Dreams (Are Made of This)": 358,
        "Out of Touch": 876,
    }
    print(len(s))
    duration=3618
    print(mixtape_graph(s,duration))
    print(mixtape_iterative_backtrack(s,duration))