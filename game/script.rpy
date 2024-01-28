

##Happy birthday, Rosie. I made this game just for us. I won't be publishing it anywhere, partially because the entirety of the text is yours, and partially because of all the music and photos
##I pirated to be able to make it exactly the way I wanted it. ((Theoretically, if you ever wanted to put it up anywhere, I could change all the music files, but it would hurt me deeply to have
##the loadup with no Deathconsciousness.)) But I also don't really want to publish it because I like having something cool that's just for me and you.
##You're 19 now, but you'll be 20 by the time you're reading this, which means it's 10 years since we've been together in this life. Really, it's more like 12 or 13, but from your 10th birthday
##I can really count ten solid years, memories of being together that are as real as anything. That's a good chunk of my childhood, and my entire adolescence, some of the hardest and most
##challenging years of my life. I'm guessing the same is true for you, too, unless you had a really hard time in between the ages of 2 and 8, and being a teenager
##was a total breeze. (I know it wasn't.) I think it's incredible how long we've been there for each other, and how easy it is. By easy I don't mean friendship isn't hard, it always is in some
##way when different people come together. That's why it's so awesome. But I mean how easy we are together, how we've known each other's patterns for years and years. I've been through breakups
##and friend breakups (which are usually worse, actually). I've passed through grade after grade, got high on hormones for years and years and years, watched the fall leaves go
##over and over again. People have stayed and left and come back. And you've been there, living alongside me, our friendship a background constant like the world's most beautiful bassline.

##That isn't a diss as to the importance of your friendship in my life, by the way. You already know I play the bass.

##And I can't say that we will always be together forever and ever and ever. I can't see the future, and I don't know what comes next. Maybe we have a huge blowout fight. Maybe we come back to
##each other three years later and it's the most beautiful moment of our lives. Maybe we drift apart over a huge distance but still think about each other almost every day.

##Maybe you pick up the phone once a year, and it's me, and things are still easy.

##Or maybe not. I don't know. I love you, and I want to keep going anyway. Follow me, and I'll follow you.

##But those ten years will always be those ten years. So easy to live, just continuing on like breathing, but such a treasure to hold and look back on.

##I totally learned beginner coding from making this game. It's super fun. I have to download ren'py on my other computer now and I have no clue if it can handle it, but I'm really attatched
##to the idea of putting a birthday card in the code. It's so awesome conceptually.

##When you used to make me birthday cards, you always used to say things like thank you for being there even though I'm STUPID!!! And I have the urge to write something similar, but
##I won't. Because I never liked the sentiment in my birthday cards. You never have to apologize for yourself. But thank you for living alongside me through my maturity and my immaturity.
##Sometimes people think I'm really mature and wise. I think you know I'm not. I just live like everybody else. Sometimes I can't see ten minutes into the future and am as vulnerable as a little
##baby. And you've been there for me during those times. Of course, sometimes I say something really cool sounding and Hit Off A Big One. I remember you hated it when people treated you
##as immature when you were little (and older!), and I didn't, at least I don't think I did. I feel similarly about the way people treat me like I've unlocked the secret to empathetic understanding
##sometimes. Spoiler alert, I have not. I just had to relearn how to hug people, like, last year.

##Also, what does any of that mean? Wisdom. Stupidity. Too mature, too immature. None of it really matters, does it?

##There's a quote written on a post-it hanging on my wall that says "Out beyond ideas of wrongdoing and rightdoing, there is a field. I'll meet you there." I wrote it down so I could give the
##post-it to you. I ended up keeping it, so I'll write it here: the sentiment still stands. I'll meet you there.

##I'm trying to say that I'm happy that you are able to grow all the aspects of your life, even when I'm not there. And I'm happy you don't shut me out of those parts of your life, and welcome
##me in as if I was just in the next room over the entire time.

##I love all the CDs you've burned for me. I drive alone at night and scream the lyrics.

##That was your birthday present to me, and this is my birthday present to you.

##I'll try to set it up so it's not on the internet, but we can both access it whenever we want. That'll probably include downloading it into your computer somehow.

##I hope you like it. I had fun making it. My favorite thing is seeing our names together on a credits screen.

##Happy 20th, Rosie.

##I'm glad we're here together.




define m = Character("Me")
define j = Character("James")
define jf = Character("Jeffery")
define mt = Character("Montgomery")


define config.main_menu_music = "audio/deepdeep.mp3"

# The game starts here.



label start:

stop music

$ renpy.movie_cutscene("movies/bike.avi")

$ renpy.movie_cutscene("movies/bimbocoding.avi")

$ renpy.movie_cutscene("movies/NOWHERE.avi")

$ renpy.movie_cutscene("movies/rosiesav.avi")

$ renpy.movie_cutscene("movies/solanac.avi")



scene bg street

play music "audio/nightbike.mp3"

"I straddled my bike, halting on the side of the rain-wet road.

It shone black in the nighttime, reflecting the sparse streetlights back at the stars."

"The attic lights were on-- not the normal ones, but the colorful ones, basking the whole room in inhuman vibrant light."

"Tracy’s room. And someone was probably up there with her."

"So {i}that{/i} was why I couldn’t sleep over. Tracy was betraying her own best friend’s interests just to get some action on a Friday night."

"Abruptly, I wheeled my bike out of the weeds and back onto the road, swiveling it away from Tracy’s house. I would find somewhere else to stay."

scene bg street 2

"The night air stung my face, dewy and harsh with moisture."

"I biked along, the whirring sound of the wheels on the road oddly soothing."

"{i}Someone could record that and make a noise machine setting,{/i} I thought. {i}Fall asleep to the sound of nowhere to go at 11:50.{/i}"

scene bg npstreet1

"I ran through people in my head. Who could I stay with tonight? Not Melanie. Not Tracy, at least for now."

"Which meant I had but one choice left: James."


scene bg npstreet2


"At the stop sign ahead, I veered right, coasting down the hill towards James’ road. He lived at the end of a cul-de-sac in a squat house with a creaky back porch."

"We’d dated for a little while last year, and we were still on good terms."

"We weren't close by any means, but he was also really weird and probably wouldn’t even mind if I showed up unannounced at midnight. The only issue with my plan was the obvious: he might have certain expectations regarding the time."

"But where else to go? I couldn’t think of anything. All at once my world began to feel small, crushingly small, intolerably small. My options were so limited. I felt claustrophobic and itchy, ready to break out and run off with strangers."

scene bg jameshouse

"James’ house loomed up ahead, painted blue and leaning jankily. All of a sudden the smallness of everything seemed endearing."

"Maybe I was just thinking about James. So known, so small, so predictable, but oddly endearing."

"I dumped my bike in the bushes and walked around the side of the house in the wet grass. James’ window was covered by a black curtain. I rapped my knuckles on the glass. "

show james nervous 1

j "No way! Julie!"

m "Hi."

j "Come in!"

scene bg jamesroom

play music "audio/digitalbath.mp3"

"I used a few cement blocks he’d haphazardly assembled into a step stool to climb inside. His room was the same as always: dark, messy, tv on but not playing anything, everything steeped in the stench of cheap weed."

show jeffery normal at left

"Jeffrey was sitting on the bed, glasses pushed onto his forehead as he read a comic. A few limp curls hung sweatily into his eyes."

"I didn’t like Jeffrey, but at least with him here, James wouldn’t try anything."

show james nervous 1 at right

j "What's up?"

"It was hard to tell if he was nervous or just genuinely excited. He fidgeted with his hair and the hem of his shirt in a way that suggested the former, but James was always a little hopped up and strange."

m "I was at Tracy’s. But she kicked me out."

jf "For Ian to go over, no doubt."

j "Make yourself comfortable."

"James hadn’t blinked in a while. He was definitely nervous. I felt bad."

"I sat in my favorite bean bag, between the window and the bed. It was always covered in dog hair. It wasn’t the best seat in his room-- that would be Jeffrey’s perch-- but it was mine."

j "I'm just gonna go shower."

"{i}Thank god."

j "I'll be back in a minute."

m "Take your time."

show jeffery glance at left

jf "Yes. Please."

"He was such a dick. God dammit."

hide james nervous 1

"James fake laughed, then left. I heard the shower turn on in the next room. I laid my head back, staring up at the posters on the ceiling. It was like saying hi to old friends."

"I used to imagine that I was in the band lineups and magazine shoots with them; these post hardcore musicians and blondes in the desert."

"My favorite was the one directly to the right of the center of the bed. It was an indie quartet, blurry and black and white, in the booth of a coffee shop. They looked like they liked each other. "

"If I could be in any band I’d never heard of, it would be that one. "

"My fantasy with no offense to James, of course. I’m sure he would’ve been perfectly fine in bed if I’d been different."

jf "So, what's been happening with you, Julie?"

show jeffery normal at left

"I didn’t take my eyes off the band snapshot. I was really good at not taking my eyes off that band snapshot."

m "You know? I'm alright."

show jeffery serious at left

"Jeffrey sat in concerned silence. He was really being awfully nice. I felt bad."

jf "I'm really sorry about Emmy and everything. I'm sorry you went through that."

m "Thanks. I appreciate that a lot."

"So that was why they were both being so weird. Emmy. But could I really blame them?"

"I tore my eyes from the picture to look up at Jeffrey. He was frowning. He looked so sad."

"My stomach sank. Had he been secretly in love with her or something? I wouldn’t be able to handle something like that. I wouldn’t be able to discuss details."

"Vagueness, dancing around it, blank apologies and boring thank yous, that I could handle. But nothing more."

"I felt bad. I felt bad, bad, bad."

show jeffery talking at left

jf "It doesn't seem real. Like things like this only happen in movies. Fake things. To fake people."

"Jeffrey went on in a way that suggested he was stoned."

"I made a noncommittal noise. He probably hadn’t had a crush on Emmy; he was just morbidly fascinated with her fate."

jf "I mean. It's like. I knew her. I actually knew her, you know? And now she's just not here anymore."

"I stewed, looking back up at the ceiling."

"Oh, to be in that indie band, where no one ever disappeared, where we all loved each other and made great art together and never, ever moved from our spots in the black and white booth."

show jeffery glance at left

jf "Sorry to blab on."

"He lay back on the bed, his head flopping towards me. His black mop of curls looked like a huge fuzzball at the corner of my eye."

jf "James just doesn't like to talk about it."

"That was probably true. James was sensitive, fragile, like a plate that came cracked."

"Drop him at the wrong angle-- say the wrong thing at the wrong time, lose your composure, or God forbid, die-- he would shatter."

"Poor Jeffrey. Dealing with peripheral grief, all on his own."

"But I didn’t really care, because that’s what it was: peripheral. He was torn up at the idea that someone he knew was gone, not at the fact it had been her.  If it was me instead, or Tracy, or anyone at all, his pain would be the same."

"Mine was different. Mine was for her."

m "So."

"I kept my tone flat and sardonic."

m "What's new with you?"

show jeffery normal at left

"He laughed darkly. I could tell he loved small talk with Death in the room."

jf "Just applying to schools. Up North, mostly."

m "What do you wanna study?"

jf "Probably film."

"He sounded a little congested."

m "Cool. I love movies."

show jeffery glance at left

"I could hear him judging me for saying movies instead of films, but I didn’t want him to think I had anything worth saying on the subject."

"Movies were everything to me. They weren’t things I liked to discuss with others, least of all Jeffrey."

hide jeffery

"We sank into silence after my conversation-killer. The music was still playing-- I was pretty sure it was Deftones at their most experimental, or a shoegaze group I didn’t know."

"Being in James’ room was nice. It was easy being who he thought I was. It was easy lying to people who’d never seen the underneath."

"{i}Like Tracy,{/i} my mind whispered. {i}Like Tracy. She saw you. She knows you. That’s why you can’t sleep over again.{/i}"

"I closed my eyes."

"I wanted to go to her house again, but it was only midnight; her guest would still be over."

"Jeffrey was, regrettably, most likely right-- it was Ian. Fucking Ian."

"Ian had big hands. That’s what Tracy liked about him."

"She liked boy hands."

"I didn’t know what was so great about Ian’s hands, aside from their size. I didn’t know what was so great about boy hands in general. Tracy was the one with the great hands; small brown birdlike fingers, soft palms, long nails coated in thin clear polish."

"I realized I was lying there imagining Tracy’s hands with my eyes closed."

show jeffery glance at left

"I snapped them open; the world shrunk. Jeffrey had sat back up, but he hadn’t returned to his comic. I hoped he hadn’t been looking at me."

"The roar of the shower stopped. We waited for James to come back in oddly amicable silence."

show james normal at right

"He returned fully clothed, in plaid pajama pants and a faded Foo Fighters shirt. This was a James usual."

j "So. You think it's definitely Ian over there at Tracy's?"

jf "Totally. Did you see them at the show this weekend? They were practically on top of each other."

show james nervous 2 at right

"James’ eyes flitted toward me nervously. He didn’t know why, but he was aware of how much I disliked Tracy’s slew of suitors."

j "Speaking of the show. Did you see that new girl there?"

jf "The blonde one with the eyes?"

m "Yeah."

show james normal at right

show jeffery normal at left

"They both turned and looked at me."

m "I talked to her. Her name's Montgomery."

scene bg showbathroom

play music "audio/yourchoicenotmine.mp3"

"I’d been hiding in the bathroom."

"Everyone I knew loved to go to the dirtiest, most obscure punk shows available, which I usually liked too, but sometimes everything dug into me like nails and I needed to escape."

"The bathroom was really shitty; covered in graffiti and stickers, only one stall and two sinks, but it was my haven."

"Tracy and I used to go in there all the time together, but she didn’t like being alone with me anymore."

show montgomery

"Then the new girl walked in. She was our age-- senior in high school-- and we’d all seen her the week before."

"It must’ve been Polly or someone who told her about the show tonight; news didn’t travel about things like this."

"She was wearing a long black trench coat. Her blond hair was scruffy and cut to her chin, at least for the most part. Her eyes were two different colors: one green, one blue."

mt "Hi."

"Her voice was low and rough."

m "Hi."

m "I'm Julie."

mt "Montgomery."

"That was the extent of our interaction. She probably didn’t remember me, but I remembered her. I liked her eyes."

"I didn’t stop thinking about her for a few days."

scene bg jamesroom

play music "audio/digitalbath.mp3"

show jeffery normal at left

show james normal at right

jf "What was her deal?"

"I shrugged."

m "I don't know. It was like a two second conversation."

jf "She seems cool. If she went to a punk show. Plus her name."

j "Montgomery."

"James liked the way certain words felt in his mouth, so he repeated them a lot. It was a trait of his that got annoying fast."

show james nervous 2 at right

j "Anyway."

j "You guys want to watch a slasher?"

"Despite his acute sensitivity and emotional frailty, James loved trashy horror."

"My theory was that he liked the over the top senselessness that allowed him to enjoy violence and hardship through an unrealistic lens."

"He couldn’t handle blood, but fake garish red painting a fake movie set was just fine by him."

"He put something on-- I didn’t pay attention to what it was called-- and he and Jeffrey sank into their familiar Friday night horror movie routine."

play music "audio/scream.mp3"

"I was ready to do the same, but the movie opened with a girl who looked my age and she was so afraid, she was screaming for help"

"and doing everything she could to get away from the killer, the killer, and I"

"started thinking about my house, and and and I started thinking and I couldn’t turn it off."

m "I'm gonna go to the bathroom."

"My legs were a little shaky. James nodded to me as I passed him."

scene bg jamesbathroom

play music "audio/digitalbathmuted.mp3"

"James’ bathroom was tiny and a bit cluttered."

"His half bath was lit by a singular window; a scruffy blue rug sat on the floor."

"The toilet was yellowed porcelain."

"The most interesting part to me were the cabinets under and over the sink. The latter were behind a sliding mirror."

"I stood on the rug, leaning against the closet door behind me where I knew the ironing table and a few other knick knacks were kept."

"I shouldn't."

"I knew I shouldn't."

"James had been so nice to me; had let me in uninvited, without question, without requirement. It was the least I could do."

"I shoved my hands under my armpits and stared at the cabinets. But it had been too long since I went through here last; there was no use fighting."

"I started at the bottom first, scanning for new items, but it was all the same-- the organs of the sink, bulbous and snaking."

"Toilet paper, unopened mouthwash, aftershave, expired hair gel, clippers with various settings, rags. Nothing new or interesting."

scene bg black

show julie eyes wide

"I stood, face to face with the mirror. My eyes were wide and unblinking. I stared myself down; my pupils held, black and flat as dinner plates."

"This was my natural state. Around others, I made my eyelids droop, casting my face into eyebagged nonchalance."

show julie eyes down

"Alone, I had crazy eyes."

scene bg jamesbathroom

"I slid the mirror away and looked at the tiny white shelves. Advil, Tylenol, Imodium, toothpaste, floss… I was of the opinion that bathrooms held a lot of people’s secrets, but James’ was as anonymous as I remembered."

"I closed the cabinet and turned, facing down the closet door."

"The knob was scratched brass, like it had been clawed. I twisted it, pulling the door toward me."

"They’d put in shelves. The ironing table was still there, leaned into the back corner. The shelves themselves were covered in towel stacks, extra sheets, cleaning supplies… a basket on the very bottom, wedged between the lowest shelf and the floor, caught my eye."

"I crouched down and tugged it out of its storage place, then immediately wished I hadn’t."

"When James and I dated, I left one of my favorite sweatshirts at his house-- a light gray crewneck with my mom’s alma mater printed over the front in thick navy blue letters. He never returned it after we broke up."

"I hadn’t even been sure I’d left it at his house; I assumed I’d just lost it somewhere."

scene bg black

play music "audio/acrophobia.mp3"

"Sitting at the bottom of the basket like some sort of shameful baby was a crude, hand sewn doll, unmistakably gray with navy blue facial features."

"The eyes were semicircles, dragging downward; my signature feigned hooded eyelids."

"The stitching was jagged and uneven. The stuffing appeared to be more fabric from my crewneck, so it was lumpy and ridged in places."

"The doll was wearing a black tunic thing. It was very obviously me."

"It was also stabbed everywhere with needles, like a demented pincushion."

"I lifted my doll self from the basket; it hung limp. My head flopped pathetically, as it was fastened to my body really poorly."

"The needles, embedded from every angle into every surface of my gray skin, seemed to be the only thing keeping my form together."

"Was this James’ attempt at a voodoo doll? What had he been trying to achieve with the needles? Was he trying to kill me or paralyze me or something?"

"I looked down at the basket. I hadn’t noticed before, as the doll was pretty attention grabbing, but there were little slips of paper littering the bottom of the woven container."

"I set the doll down gently, letting her balance on the ends of the needles on her back. She seemed to levitate an inch off the tile floor."

"I picked up a slip of paper and unfolded it. Written in James’ tiny, cramped scrawl were the words {i}make it hurt{/i}."

$ renpy.movie_cutscene("movies/makeithurt.avi")

play music "audio/phobia2.mp3"

"I folded the paper back up and placed it in the basket. Then, delicately, I picked up my sweater doll and cradled her in my hands."

"She smiled up at me, her half open eyes oddly mean-spirited. I placed her back into the basket and shoved the whole thing under the shelf again."

"I closed the closet door and stared at it. It felt like bugs were crawling up and down my spine. Needles everywhere, over my head, down my arms. My mom’s old sweatshirt."

"I blinked. I blinked again. {i}Make it hurt{/i}. I had to get out of here."

scene bg jamesroom

show james red normal at right

show jeffery red at left

play music "audio/scream.mp3"

"I pulled my phone out of my pocket and walked back into James’ room. Whatever was happening on the TV was bloody, and both boys’ faces were washed over in red."

"James looked over at me from his chair. He was so jittery. Maybe the voodoo doll he’d made of me was the reason."

m "Tracy's calling me. Gotta go. Thanks for having me."

show james red suprised at right

"Jeffrey gave me an affectionate little wave. James nodded at me, smiling with his teeth again. {i}Make it hurt.{/i}"

scene bg jameshouse

play music "audio/nightbike.mp3"

"I crawled out of his window and shoved it shut, breathing hard. {i}It fucking worked, James. It fucking hurts.{/i}"

"I ran to my bike, hauled it upright, and sped off into the night."

scene bg npstreet2

"I wanted to go to Tracy’s, but Ian would still be there."

"I wanted Tracy."

"I shook my head at the thought; I hated thinking things like that, all weak and soft bellied, needy like a traumatized child."

"I could do it alone."

"I was whole alone."

"I didn't need Tracy."

"I didn't need anyone."

scene bg black

play music "audio/nightbike.mp3"

"I squeezed my eyes shut. I didn't need anyone."



$ renpy.movie_cutscene("movies/endscreen.avi")

$ renpy.movie_cutscene("movies/gameover.avi")

$ renpy.movie_cutscene("movies/endgif.avi")


    # This ends the game.

return
