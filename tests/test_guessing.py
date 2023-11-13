import pytest

from guestrrday.guestrrday import year_guesser
from guestrrday.track import track

def test_many_tracks():
	dg = year_guesser()
	global GUESS_LIST
	for i in GUESS_LIST:
		inp, out  = i
		tr = track(inp)
		assert dg.guess_track(tr) == out
		
		
GUESS_LIST = [ 
("001. X-Press 2 Ft. David Byrne - Lazy" , (2002, 'Skint')),
("002. John Digweed - Heaven Scent" , (1999, 'Bedrock Records')),
("003. Skyy - High" , (1980, 'Derby')),
("004. Inner Life - I'm Caught Up (In a One Night Love Affair) 1979" , (1979, 'Prelude Records')),
("005. Kerri Chandler – Bar A Thym" , (2005, 'NRK Sound Division')),
("006. Breathe (feat. Erire) (Lexicon Avenue Remix)" , (2001, 'Kaos Records')),
("007. Egberto Gismonti - Selva Amazônica ｜ FMCB 5" , (1979, 'ECM Records')),
("008. The Isley Brothers - Fight the Power, Pts. 1 & 2" , (1991, 'Rhino Records')),
("009. The salsoul orchestra - getaway" , (1977, 'Salsoul Records')),
("010. Loleatta Holloway - Hit and Run (Walter Gibbons 12＂ Remix)" , (1977, 'Gold Mind Records')),
("011. Silver Hollow" , (1978, 'ECM Records')),
("012. The Bucketheads - The Bomb" , (1994, 'Henry Street Music')),
("013. WAR - Low Rider" , (1975, 'United Artists Records')),
("014. Eberhard Weber - Death in the Carwash" , (1982, 'ECM Records')),
("015. Masters At Work feat. India - To Be In Love (Original MAW Mix)" , (1997, 'MAW Records')),
("016. Skyy - Call Me (Extended)" , (1981, 'Salsoul Records')),
("017. The O'Jays - Love Train" , (1972, 'Philadelphia International Records')),
("018. Yasunao Tone - Solo for Wounded • Part II" , (1997, 'Tzadik')),
("019. Bill Connors Trio A Pedal 1985" , None),
("020. Ghostface Killah - Mighty Healthy" , (1998, 'Epic Street')),
("021. Instant Funk - Slap Slap Lickedy Lap" , (1979, 'Salsoul Records')),
("022. Ohio Players  -  Fire" , (1974, 'Mercury')),
("023. Roger Sanchez - Another Chance (Directors Cut)" , (2001, 'Dance Pool')),
("024. Scanner - Mass Observation (Expanded)" , (1994, 'Ash International')),
("025. CANDIDO. ＂Dancin' And Prancin'＂. 1979. Original 12＂ Mix." , (1979, 'Salsoul Records')),
("026. Ikue Mori – Labyrinth (CD)" , (2001, 'Tzadik')),
("027. The Meters - Just Kissed My Baby" , (1976, 'Reprise Records')),
("028. The Roots - The Next Movement" , (1999, 'MCA Records')),
("029. Todd Terry Ft. Martha Wash & Jocelyn Brown - Something Goin' On (Tee's Remix)" , (2006, 'CD Pool')),
("030. CoH   Patherns   Path 4" , (2006, 'Raster-Noton')),
("031. JOHNNY GRIFFIN QUARTET - Autumn Leaves - Amazing piano solo - Rare live recording" , None),
("032. Lauryn Hill - Lost Ones" , (1998, 'Ruffhouse Records')),
("033. Theo Parrish - Falling Up (Carl Craig Remix)" , (2005, 'Not On Label')),
("034. Tower of Power - What is Hip (Album Version)" , (1973, 'Warner Bros. Records')),
("035. DMX - Ruff Ryders' Anthem" , (1998, 'Def Jam Recordings')),
("036. Richard Devine-Floccus" , (2003, 'Schematic')),
("037. The Commodores-Brick House" , (1977, 'Motown')),
("038. Al Green - Let's Stay Together" , (1971, 'London Records')),
("039. Black Star (Mos Def & Talib Kweli) - Definition" , (1998, 'Rawkus')),
("040. Curtis Mayfield - Superfly" , (1972, 'Curtom')),
("041. Jay-Z - U Don't Know" , (2001, 'Roc-A-Fella Records')),
("042. Nas - It Ain't Hard to Tell" , (1994, 'Columbia')),
("043. The Gap Band - Outstanding" , (1982, 'Total Experience Records')),
("044. Parliament - Give Up The Funk (Tear The Roof Off The Sucker)" , (1976, 'Casablanca')),
("045. The Notorious B.I.G. - Kick in the Door" , (1997, 'Bad Boy Entertainment')),
("046. Big Pun - Twinz ft. Fat Joe" , (1997, 'Terror Squad Production')),
("047. Stevie Wonder - Higher Ground" , (1973, 'Tamla Motown')),
("048. Common - The 6th Sense ft. Bilal" , (2000, 'MCA Records')),
("049. Raekwon - Incarcerated Scarfaces" , (1995, 'Loud Records')),
("050. A Tribe Called Quest - Award Tour" , (1993, 'Jive')),
("051. Nas - Nas Is Like" , (1999, 'Columbia')),
("052. Nina Simone - Backlash Blues" , (1967, 'RCA Victor')),
("053. Nina Simone - Don't You Pay Them No Mind" , (1966, 'Philips')),
("054. Nina Simone： Pirate Jenny" , (1988, 'Grind')),
("055. Good Girls Don't by THE KNACK" , (1979, 'Capitol Records')),
("056. Nina Simone - Mississippi Goddam (Live At Carnegie Hall, New York, 1964 ⧸ Audio)" , (1965, 'Philips')),
("057. ben webster caravan" , (1997, 'RCA Victor')),
("058. Nina Simone -  Ain't Got No ⧸ I Got Life (Live 1968)" , (1968, 'RCA Victor')),
("059. The Jam   Precious 12 Inch version" , (2003, 'Central Station')),
("060. Charlie Parker (1946) FIRST RECORDING" , (2001, 'Definitive Records')),
("061. NINA SIMONE - Sinnerman (1965)" , (1968, 'Philips')),
("062. the clash - train in vain (ext version)" , (1979, 'Epic')),
("063. Nina Simone - I put a spell on you" , (1965, 'Philips')),
("064. Roxy Music - Angel Eyes (1979) full 12” Single" , (1979, 'Polydor')),
("065. Thelonious Monk - Straight No Chaser 1951" , (1983, 'Mosaic Records')),
("066. BIGTOWN PLAYBOY - Eddie Taylor" , (1956, 'Vee Jay Records')),
("067. Fleetwood Mac - Everywhere (12 Inch Version) 05_47" , (1987, 'Warner Bros. Records')),
("068. Miles Davis - Freddie Freeloader" , (1961, 'Fontana')),
("069. Nina Simone - To Be Young, Gifted and Black (Live at Philharmonic Hall, New York, NY - October 1969)" , (1969, 'RCA Victor')),
("070. Cheap Trick - Surrender. (Guardians of the Galaxy) Vol. 2" , (1978, 'Epic')),
("071. John Coltrane - Naima (Album：Giant Steps) 1959" , (1960, 'Atlantic')),
("072. Nina Simone - Don't Let Me Be Misunderstood" , (1964, 'Philips')),
("073. Smokey Smothers - Come on rock little girl" , (1962, 'King Records')),
("074. 1933 HITS ARCHIVE： Sophisticated Lady - Duke Ellington (Brunswick version)" , None),
("075. Big Jack  Johnson   Catfish Blues" , (1979, 'Albatros')),
("076. Blondie - Heart Of Glass (Original 12'' Instrumental Version)" , (1978, 'Chrysalis')),
("077. Nina Simone - Here Comes the Sun (Audio)" , (1971, 'RCA')),
("078. Billy ＂The Kid＂ Emerson - Red Hot" , (1955, 'Sun')),
("079. David Bowie - Look Back In Anger" , (1979, 'RCA')),
("080. Miles Davis - A NIGHT IN TUNISIA - Paparelli-Dizzy Gillespie - 1955" , (1955, 'Prestige')),
("081. Nina Simone Sunday In Savannah (Live)" , (2005, 'Kultur')),
("082. Eddie Kirkland - Train Done Gone" , (1961, 'Tru-Sound')),
("083. Max Roach Quintet - Bemsha Swing" , (1964, 'Mercury')),
("084. Pretenders - Brass In Pocket (Extended)" , (1979, 'Real Records')),
("085. Blues In The Dark , Little George Smith" , None),
("086. Ray Charles - A Fool For You (From ＂Legends of Rock 'N' Roll＂ DVD)" , (1956, 'Atlantic')),
("087. The Stone Roses - Waterfall" , (1989, 'Silvertone Records')),
("088. Happy Mondays - Hallelujah" , (1990, 'Virgin')),
("089. Harmonica Hinds - Berlin (1977) Part 1" , (2012, 'Legacy')),
("090. Howlin' Wolf - I Ain't Superstitious (1961)" , (1962, 'Chess')),
("091. The Charlatans - Polar Bear (Remastered)" , (1990, 'Situation Two')),
("092. Inspiral Carpets - Joe" , (1989, 'Cow')),
("093. Jerry McCain - That's What They Want" , (1955, 'Excello')),
("094. Jerry Boogie McCain - I'm A King Bee" , (1996, 'Black & Allright')),
("095. Mock Turtles - Lay Me Down" , (1990, 'Imaginary Records')),
("096. Left Hand Frank and his Blues Band, Blues won't let me be" , None),
("097. THE FARM 'STEPPIN STONE'" , (1991, 'Sire')),
("098. Homesick James,  ＂Set a Date＂ 1965" , (1965, 'Sue Records')),
("099. James - Sometimes" , (1988, 'SST Records')),
("100. John Primer  ~ '' Blue And Lonesome ''  2013" , (2013, 'Delta Groove Music,')),
("101. Primal Scream - Come Together" , (1990, 'Creation Records')),
("102. Northside - Take Five" , (1991, 'Festival Records')),
("103. The Soup Dragons - Divine Thing (Remastered)" , (1992, 'Big Life')),
("104. The Stone Roses - She Bangs the Drums" , (1989, 'Silvertone Records')),
("105. Happy Mondays - Loose Fit" , (1991, 'Factory')),
("106. THE CHARLATANS - Indian rope" , (1989, 'Dead Dead Good'))]