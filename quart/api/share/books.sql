-- $ sqlite3 ./var/books.db < ./share/books.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    id INTEGER primary key,
    published INT,
    author VARCHAR,
    title VARCHAR,       
    first_sentence VARCHAR,
    UNIQUE(published, author, title)
);
INSERT INTO books(published, author, title, first_sentence) VALUES(2014,'Ann Leckie','Ancillary Justice','The body lay naked and facedown, a deathly gray, spatters of blood staining the snow around it.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2013,'John Scalzi','Redshirts','From the top of the large boulder he sat on, Ensign Tom Davis looked across the expanse of the cave, toward Captain Lucius Abernathy, Science Officer Q’eeng and Chief Engineer Paul West perched on a second, larger boulder, and thought, Well, this sucks.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2012,'Jo Walton','Among Others','The Phurnacite factory in Abercwmboi killed all the trees for two miles around.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2011,'Connie Willis','Blackout, All Clear (Vol. 2 - Blackout)','By noon Michael and Merope still hadn’t returned from Stepney, and Polly was beginning to get really worried.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2010,'Paolo Bacigalupi','The Windup Girl','“No! I don’t want the mangosteen.”');
INSERT INTO books(published, author, title, first_sentence) VALUES(2010,'China Mieville','The City & The City','I could not see the street or much of the estate.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2009,'Neil Gaiman','The Graveyard Book','Nobody Owens, known to his friends as Bod, is a normal boy.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2008,'Michael Chabon','The Yiddish Policemen''s Union','Nine months Landsman’s been flopping at the Hotel Zamenhof without any of his fellow residents managing to get themselves murdered.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2007,'Vernor Vinge','Rainbows End','The first bit of dumb luck came disguised as a public embarrassment for the European Center for Defense Against Disease.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2006,'Robert Charles Wilson','Spin','One night in October when he was ten years old, Tyler Dupree stood in his back yard and watched the stars go out.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2005,'Susanna Clarke','Jonathan Strange and Mr. Norrell','Some years ago there was in the city of York a society of magicians.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2004,'Lois McMaster Bujold','Paladin of Souls','Sta leaned forward between the crenellations atop the gate tower, the stone gritty beneath her pale hands, and watched in numb exhaustion as the final mourning party cleared the castle gate below.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2003,'Robert J. Sawyer','Hominids','The blackness was absolute.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2002,'Neil Gaiman','American Gods','Shadow had done three years in prison.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2001,'J. K. Rowling','Harry Potter and the Goblet of Fire','The villagers of Little Hangleton still called it “the Riddle House,” even though it had been many years since the Riddle family had lived there.');
INSERT INTO books(published, author, title, first_sentence) VALUES(2000,'Vernor Vinge','A Deepness in the Sky','The manhunt extended across more than one hundred light-years and eight centuries.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1999,'Connie Willis','To Say Nothing of the Dog','There were five of us—Carruthers and the new recruit and myself, and Mr. Spivens and the verger.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1998,'Joe Haldeman','Forever Peace','It was not quite completely dark, thin blue moonlight threading down through the canopy of leaves.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1997,'Kim Stanley Robinson','Blue Mars','Mars is free now. We’re on our own. No one tells us what to do.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1996,'Neal Stephenson','The Diamond Age','The bells of St. Mark''s were ringing changes up on the mountain when Bud skated over to the mod parlor to upgrade his skull gun.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1995,'Lois McMaster Bujold','Mirror Dance','The row of comconsole booths lining the passenger concourse of Escobar''s largest commercial orbital transfer station had mirrored doors, divided into diagonal sections by rainbow-colored lines of lights.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1994,'Kim Stanley Robinson','Green Mars','The point is not to make another Earth. Not another Alaska or Tibet, not a Vermont nor a Venice, not even an Antarctica. The point is to make something new and strange, something Martian.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1993,'Vernor Vinge','A Fire Upon the Deep','The coldsleep itself was dreamless.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1993,'Connie Willis','Doomsday Book','Mr. Dunworthy opened the door to the laboratory and his spectacles promptly steamed up.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1992,'Lois McMaster Bujold','Barrayar','I am afraid.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1991,'Lois McMaster Bujold','The Vor Game','"Ship duty!" chortled the ensign four ahead of Miles in line.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1990,'Dan Simmons','Hyperion','The Consul awoke with the peculiar headache, dry throat, and sense of having forgotten a thousand dreams which only periods in cryogenic fugue could bring.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1989,'C. J. Cherryh','Cyteen','It was from the air that the rawness of the land showed most: vast tracts where humanity had as yet made no difference, deserts unclaimed, stark as moons, scrag and woolwood thickets unexplored except by orbiting radar.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1988,'David Brin','The Uplift War','There had never been such traffic at Port Helenia’s sleepy landing field—not in all the years Fiben Bolger had lived here.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1987,'Orson Scott Card','Speaker for the Dead','Rooter was at once the most difficult and the most helpful of the pequeninos.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1986,'Orson Scott Card','Ender''s Game','The monitor lady smiled very nicely and tousled his hair and said, “Andrew, I suppose by now you’re just absolutely sick of having that horrid monitor.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1985,'William Gibson','Neuromancer','The sky above the port was the color of television, tuned to a dead channel.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1984,'David Brin','Startide Rising','Fins had been making wisecracks about human beings for thousands of years.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1983,'Isaac Asimov','Foundation''s Edge','“I don’t believe it, of course,” said Golan Trevize, standing on the wide steps of Seldon Hall and looking out over the city as it sparkled in the sunlight.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1982,'C. J. Cherryh','Downbelow Station','The stars, like all man’s other ventures, were an obvious impracticality, as rash and improbable an ambition as the first venture of man onto Earth’s own great oceans, or into the air, or into space.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1981,'Joan D. Vinge','The Snow Queen','Here on Tiamat, where there is more water than land, the sharp edge between ocean and sky is blurred; the two merge into one.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1980,'Arthur C. Clarke','The Fountains of Paradise','The crown grew heavier with each passing year.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1979,'Vonda N. McIntyre','Dreamsnake','The little boy was frightened.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1978,'Frederik Pohl','Gateway','My name is Robinette Broadhead, in spite of which I am male.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1977,'Kate Wilhelm','Where Late the Sweet Birds Sang','What David always hated most about the Sumner family dinners was the way everyone talked about him as if he were not there.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1976,'Joe Haldeman','The Forever War','“Tonight we’re going to show you eight silent ways to kill a man.”');
INSERT INTO books(published, author, title, first_sentence) VALUES(1975,'Ursula K. Le Guin','The Dispossessed','There was a wall.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1974,'Arthur C. Clarke','Rendezvous with Rama','Sooner or later, it was bound to happen.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1973,'Isaac Asimov','The Gods Themselves','“Let me give you a lesson in practical politics.”');
INSERT INTO books(published, author, title, first_sentence) VALUES(1972,'Philip Jose Farmer','To Your Scattered Bodies Go','All those who ever lived on Earth have found themselves resurrected--healthy, young, and naked as newborns--on the grassy banks of a mighty river, in a world unknown.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1971,'Larry Niven','Ringworld','In the nighttime heart of Beirut, in one of a row of general-address transfer booths, Louis Wu flicked into reality.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1970,'Ursula K. Le Guin','The Left Hand of Darkness','I''ll make my report as if I told a story, for I was taught as a child on my homeworld that Truth is a matter of the imagination.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1969,'John Brunner','Stand on Zanzibar','SCANALYZE MY NAME');
INSERT INTO books(published, author, title, first_sentence) VALUES(1968,'Roger Zelazny','Lord of Light','It is said that fifty-three years after his liberation he returned from the Golden Cloud, to take up once again the gauntlet of Heaven, to oppose the Order of Life and the gods who ordained it so.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1967,'Robert A. Heinlein','The Moon Is a Harsh Mistress','I see in Lunaya Pravda that Luna City Council has passed on first reading a bill to examine, license, inspect—and tax—public food vendors operating inside municipal pressure.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1966,'Roger Zelazny','And Call Me Conrad (aka. This Immortal)','“You are a Kallikanzaros,” she announced suddenly.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1966,'Frank Herbert','Dune','In the week before their departure to Arrakis, when all the final scurrying about had reached a nearly unbearable frenzy, an old crone came to visit the mother of the boy, Paul.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1965,'Fritz Leiber','The Wanderer','Some stories of terror and the supernormal start with a moonlit face at a diamond-paned window, or an old document in spidery handwriting, or the baying of a hound across lonely moors.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1964,'Clifford D. Simak','Here Gather the Stars','The noise was ended now.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1963,'Philip K. Dick','The Man in the High Castle','For a week Mr. R. Childan had been anxiously watching the mail.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1962,'Robert A. Heinlein','Stranger in a Strange Land','Once upon a time when the world was young there was a Martian named Smith.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1961,'Walter M. Miller Jr.','A Canticle for Leibowitz','Brother Francis Gerard of Utah might never have discovered the blessed documents, had it not been for the pilgrim with girded loins who appeared during that young novice’s Lenten fast in the desert.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1960,'Robert A. Heinlein','Starship Troopers','I always get the shakes before a drop.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1959,'James Blish','A Case Of Conscience','The stone door slammed.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1958,'Fritz Leiber','The Big Time','My name is Greta Forzane.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1956,'Robert A. Heinlein','Double Star','If a man walks in dressed like a hick and acting as if he owned the place, he’s a spaceman.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1955,'Mark Clifton and Frank Riley','They''d Rather Be Right','Just ahead, on Third Street, the massive facade of San Francisco''s Southern Pacific depot loomed, half hidden in the swirling fog and January twilight.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1954,'Ray Bradbury','Fahrenheit 451','It was a pleasure to burn.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1953,'Alfred Bester','The Demolished Man','Explosion!');
INSERT INTO books(published, author, title, first_sentence) VALUES(1951,'Robert A. Heinlein','Farmer in the Sky','Our troop had been up in the High Sierras that day and we were late getting back.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1946,'Isaac Asimov','The Mule','Bel Riose traveled without escort, which is not what court etiquette prescribes for the head of a fleet stationed in a yet-sullen stellar system on the Marches of the Galactic Empire.');
INSERT INTO books(published, author, title, first_sentence) VALUES(1939,'T. H. White','The Sword in the Stone (Part 1 of The Once and Future King)','ender');
COMMIT;
