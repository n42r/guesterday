import pytest

from guestrrday.track import track		

def test_track_init_correct_clean_title_no_filename():
	t = track('02. Prince - Musicology (Timelife Mix)')
	assert t.get_filename_path() is None \
		and t.get_title() == 'Prince - Musicology (Timelife Mix)' \
		and t.get_artist() == 'Prince' \
		and t.get_song_title() == 'Musicology' \
		and t.get_track() == 2 \
		and t.get_qualifier() == 'Timelife Mix' \
		and t.get_year() == None

def test_track_init_correct_dirty1_fixed_title_no_filename():
	t = track('02. Prince _ Musicology (Timelife Mix)')
	assert t.get_filename_path() is None \
		and t.get_title() == 'Prince - Musicology (Timelife Mix)' \
		and t.get_artist() == 'Prince' \
		and t.get_song_title() == 'Musicology' \
		and t.get_track() == 2 \
		and t.get_qualifier() == 'Timelife Mix' \
		and t.get_year() == None


def test_track_init_correct_dirty2_fixed_title_no_filename():
	t = track('2 Prince  Musicology (Timelife Mix)')
	assert t.get_filename_path() is None \
		and t.get_title() == 'Prince - Musicology (Timelife Mix)' \
		and t.get_artist() == 'Prince' \
		and t.get_song_title() == 'Musicology' \
		and t.get_track() == 2 \
		and t.get_qualifier() == 'Timelife Mix' \
		and t.get_year() == None


def test_track_init_correct_dirty2_fixed_title_no_filename():
	t = track('032. Lydia Lunch ＂Mechanical Flattery＂ 1980')
	assert t.get_filename_path() is None \
		and t.get_title() == 'Lydia Lunch - Mechanical Flattery 1980' \
		and t.get_artist() == 'Lydia Lunch' \
		and t.get_song_title() == 'Mechanical Flattery 1980' \
		and t.get_track() == 32 \
		and t.get_qualifier() == None \
		and t.get_year() == None

		
def test_track_init_correct_filename():
#	MyFolder\MyAlbum\02. Prince - Musicology (Timelife Mix).mp3
	from pathlib import Path
	Path('tests/haha - meme (ds).mp3').touch()
	t = track('tests/haha - meme (ds).mp3')
	assert(t.get_filename_path() == 'tests/haha - meme (ds).mp3')
	Path('tests/haha - meme (ds).mp3').unlink()
	
def test_many_tracks():
	global TRACK_LIST
	for i in TRACK_LIST:
		inp, out  = i
		tr = track(inp)
		assert tr.__dict__ == dict(out)
	


TRACK_LIST = [
("001. X-Press 2 Ft. David Byrne - Lazy" , {'filename_path': None, 'title': 'X-Press 2 Ft. David Byrne - Lazy', 'track': 1, 'artist': 'X-Press 2 Ft. David Byrne', 'year': None, 'qualifier': None, 'song_title': 'Lazy', 'id': None}),
("002. John Digweed - Heaven Scent" , {'filename_path': None, 'title': 'John Digweed - Heaven Scent', 'track': 2, 'artist': 'John Digweed', 'year': None, 'qualifier': None, 'song_title': 'Heaven Scent', 'id': None}),
("003. Skyy - High" , {'filename_path': None, 'title': 'Skyy - High', 'track': 3, 'artist': 'Skyy', 'year': None, 'qualifier': None, 'song_title': 'High', 'id': None}),
("004. Inner Life - I'm Caught Up (In a One Night Love Affair) 1979" , {'filename_path': None, 'title': "Inner Life - I'm Caught Up (In a One Night Love Affair) 1979", 'track': 4, 'artist': 'Inner Life', 'year': None, 'qualifier': None, 'song_title': "I'm Caught Up (In a One Night Love Affair) 1979", 'id': None}),
("005. Kerri Chandler – Bar A Thym" , {'filename_path': None, 'title': 'Kerri Chandler - Bar A Thym', 'track': 5, 'artist': 'Kerri Chandler', 'year': None, 'qualifier': None, 'song_title': 'Bar A Thym', 'id': None}),
("006. Breathe (feat. Erire) (Lexicon Avenue Remix)" , {'filename_path': None, 'title': '006. Breathe (feat. Erire) (Lexicon Avenue Remix)', 'track': None, 'artist': '006. Breathe (feat. Erire) (Lexicon Avenue Remix)', 'year': None, 'qualifier': None, 'song_title': '006. Breathe (feat. Erire) (Lexicon Avenue Remix)', 'id': None}),
("007. Egberto Gismonti - Selva Amazônica ｜ FMCB 5" , {'filename_path': None, 'title': 'Egberto Gismonti - Selva Amazonica | FMCB 5', 'track': 7, 'artist': 'Egberto Gismonti', 'year': None, 'qualifier': None, 'song_title': 'Selva Amazonica | FMCB 5', 'id': None}),
("008. The Isley Brothers - Fight the Power, Pts. 1 & 2" , {'filename_path': None, 'title': 'The Isley Brothers - Fight the Power, Pts. 1 & 2', 'track': 8, 'artist': 'The Isley Brothers', 'year': None, 'qualifier': None, 'song_title': 'Fight the Power, Pts. 1 & 2', 'id': None}),
("009. The salsoul orchestra - getaway" , {'filename_path': None, 'title': 'The salsoul orchestra - getaway', 'track': 9, 'artist': 'The salsoul orchestra', 'year': None, 'qualifier': None, 'song_title': 'getaway', 'id': None}),
("010. Loleatta Holloway - Hit and Run (Walter Gibbons 12＂ Remix)" , {'filename_path': None, 'title': 'Loleatta Holloway - Hit & Run (Walter Gibbons 12 Remix)', 'track': 10, 'artist': 'Loleatta Holloway', 'year': None, 'qualifier': 'Walter Gibbons 12 Remix', 'song_title': 'Hit & Run', 'id': None}),
("011. Silver Hollow" , {'filename_path': None, 'title': '011. Silver Hollow', 'track': None, 'artist': '011. Silver Hollow', 'year': None, 'qualifier': None, 'song_title': '011. Silver Hollow', 'id': None}),
("012. The Bucketheads - The Bomb" , {'filename_path': None, 'title': 'The Bucketheads - The Bomb', 'track': 12, 'artist': 'The Bucketheads', 'year': None, 'qualifier': None, 'song_title': 'The Bomb', 'id': None}),
("013. WAR - Low Rider" , {'filename_path': None, 'title': 'WAR - Low Rider', 'track': 13, 'artist': 'WAR', 'year': None, 'qualifier': None, 'song_title': 'Low Rider', 'id': None}),
("014. Eberhard Weber - Death in the Carwash" , {'filename_path': None, 'title': 'Eberhard Weber - Death in the Carwash', 'track': 14, 'artist': 'Eberhard Weber', 'year': None, 'qualifier': None, 'song_title': 'Death in the Carwash', 'id': None}),
("015. Masters At Work feat. India - To Be In Love (Original MAW Mix)" , {'filename_path': None, 'title': 'Masters At Work &  India - To Be In Love (Original MAW Mix)', 'track': 15, 'artist': 'Masters At Work &  India', 'year': None, 'qualifier': 'Original MAW Mix', 'song_title': 'To Be In Love', 'id': None}),
("016. Skyy - Call Me (Extended)" , {'filename_path': None, 'title': 'Skyy - Call Me (Extended)', 'track': 16, 'artist': 'Skyy', 'year': None, 'qualifier': 'Extended', 'song_title': 'Call Me', 'id': None}),
("017. The O'Jays - Love Train" , {'filename_path': None, 'title': "The O'Jays - Love Train", 'track': 17, 'artist': "The O'Jays", 'year': None, 'qualifier': None, 'song_title': 'Love Train', 'id': None}),
("018. Yasunao Tone - Solo for Wounded • Part II" , {'filename_path': None, 'title': 'Yasunao Tone - Solo for Wounded  Part II', 'track': 18, 'artist': 'Yasunao Tone', 'year': None, 'qualifier': None, 'song_title': 'Solo for Wounded  Part II', 'id': None}),
("019. Bill Connors Trio A Pedal 1985" , {'filename_path': None, 'title': '019. Bill Connors Trio A Pedal 1985', 'track': None, 'artist': '019. Bill Connors Trio A Pedal 1985', 'year': None, 'qualifier': None, 'song_title': '019. Bill Connors Trio A Pedal 1985', 'id': None}),
("020. Ghostface Killah - Mighty Healthy" , {'filename_path': None, 'title': 'Ghostface Killah - Mighty Healthy', 'track': 20, 'artist': 'Ghostface Killah', 'year': None, 'qualifier': None, 'song_title': 'Mighty Healthy', 'id': None}),
("021. Instant Funk - Slap Slap Lickedy Lap" , {'filename_path': None, 'title': 'Instant Funk - Slap Slap Lickedy Lap', 'track': 21, 'artist': 'Instant Funk', 'year': None, 'qualifier': None, 'song_title': 'Slap Slap Lickedy Lap', 'id': None}),
("022. Ohio Players  -  Fire" , {'filename_path': None, 'title': 'Ohio Players - Fire', 'track': 22, 'artist': 'Ohio Players', 'year': None, 'qualifier': None, 'song_title': 'Fire', 'id': None}),
("023. Roger Sanchez - Another Chance (Directors Cut)" , {'filename_path': None, 'title': 'Roger Sanchez - Another Chance (Directors Cut)', 'track': 23, 'artist': 'Roger Sanchez', 'year': None, 'qualifier': 'Directors Cut', 'song_title': 'Another Chance', 'id': None}),
("024. Scanner - Mass Observation (Expanded)" , {'filename_path': None, 'title': 'Scanner - Mass Observation (Expanded)', 'track': 24, 'artist': 'Scanner', 'year': None, 'qualifier': 'Expanded', 'song_title': 'Mass Observation', 'id': None}),
("025. CANDIDO. ＂Dancin' And Prancin'＂. 1979. Original 12＂ Mix." , {'filename_path': None, 'title': "CANDIDO. - Dancin' And Prancin'. 1979. Original 12 Mix.", 'track': 25, 'artist': 'CANDIDO.', 'year': None, 'qualifier': None, 'song_title': "Dancin' And Prancin'. 1979. Original 12 Mix.", 'id': None}),
("026. Ikue Mori – Labyrinth (CD)" , {'filename_path': None, 'title': 'Ikue Mori - Labyrinth (CD)', 'track': 26, 'artist': 'Ikue Mori', 'year': None, 'qualifier': 'CD', 'song_title': 'Labyrinth', 'id': None}),
("027. The Meters - Just Kissed My Baby" , {'filename_path': None, 'title': 'The Meters - Just Kissed My Baby', 'track': 27, 'artist': 'The Meters', 'year': None, 'qualifier': None, 'song_title': 'Just Kissed My Baby', 'id': None}),
("028. The Roots - The Next Movement" , {'filename_path': None, 'title': 'The Roots - The Next Movement', 'track': 28, 'artist': 'The Roots', 'year': None, 'qualifier': None, 'song_title': 'The Next Movement', 'id': None}),
("029. Todd Terry Ft. Martha Wash & Jocelyn Brown - Something Goin' On (Tee's Remix)" , {'filename_path': None, 'title': "Todd Terry Ft. Martha Wash & Jocelyn Brown - Something Goin' On (Tee's Remix)", 'track': 29, 'artist': 'Todd Terry Ft. Martha Wash & Jocelyn Brown', 'year': None, 'qualifier': "Tee's Remix", 'song_title': "Something Goin' On", 'id': None}),
("030. CoH   Patherns   Path 4" , {'filename_path': None, 'title': 'CoH - Patherns   Path 4', 'track': 30, 'artist': 'CoH', 'year': None, 'qualifier': None, 'song_title': 'Patherns   Path 4', 'id': None}),
("031. JOHNNY GRIFFIN QUARTET - Autumn Leaves - Amazing piano solo - Rare live recording" , {'filename_path': None, 'title': 'JOHNNY GRIFFIN QUARTET - Autumn Leaves - Amazing piano solo - Rare live recording', 'track': 31, 'artist': 'JOHNNY GRIFFIN QUARTET - Autumn Leaves - Amazing piano solo', 'year': None, 'qualifier': None, 'song_title': 'Rare live recording', 'id': None}),
("032. Lauryn Hill - Lost Ones" , {'filename_path': None, 'title': 'Lauryn Hill - Lost Ones', 'track': 32, 'artist': 'Lauryn Hill', 'year': None, 'qualifier': None, 'song_title': 'Lost Ones', 'id': None}),
("033. Theo Parrish - Falling Up (Carl Craig Remix)" , {'filename_path': None, 'title': 'Theo Parrish - Falling Up (Carl Craig Remix)', 'track': 33, 'artist': 'Theo Parrish', 'year': None, 'qualifier': 'Carl Craig Remix', 'song_title': 'Falling Up', 'id': None}),
("034. Tower of Power - What is Hip (Album Version)" , {'filename_path': None, 'title': 'Tower of Power - What is Hip (Album Version)', 'track': 34, 'artist': 'Tower of Power', 'year': None, 'qualifier': 'Album Version', 'song_title': 'What is Hip', 'id': None}),
("035. DMX - Ruff Ryders' Anthem" , {'filename_path': None, 'title': "DMX - Ruff Ryders' Anthem", 'track': 35, 'artist': 'DMX', 'year': None, 'qualifier': None, 'song_title': "Ruff Ryders' Anthem", 'id': None}),
("036. Richard Devine-Floccus" , {'filename_path': None, 'title': 'Richard Devine - Floccus', 'track': 36, 'artist': 'Richard Devine', 'year': None, 'qualifier': None, 'song_title': 'Floccus', 'id': None}),
("037. The Commodores-Brick House" , {'filename_path': None, 'title': 'The Commodores - Brick House', 'track': 37, 'artist': 'The Commodores', 'year': None, 'qualifier': None, 'song_title': 'Brick House', 'id': None}),
("038. Al Green - Let's Stay Together" , {'filename_path': None, 'title': "Al Green - Let's Stay Together", 'track': 38, 'artist': 'Al Green', 'year': None, 'qualifier': None, 'song_title': "Let's Stay Together", 'id': None}),
("039. Black Star (Mos Def & Talib Kweli) - Definition" , {'filename_path': None, 'title': 'Black Star (Mos Def & Talib Kweli) - Definition', 'track': 39, 'artist': 'Black Star (Mos Def & Talib Kweli)', 'year': None, 'qualifier': None, 'song_title': 'Definition', 'id': None}),
("040. Curtis Mayfield - Superfly" , {'filename_path': None, 'title': 'Curtis Mayfield - Superfly', 'track': 40, 'artist': 'Curtis Mayfield', 'year': None, 'qualifier': None, 'song_title': 'Superfly', 'id': None}),
("041. Jay-Z - U Don't Know" , {'filename_path': None, 'title': "Jay-Z - U Don't Know", 'track': 41, 'artist': 'Jay-Z', 'year': None, 'qualifier': None, 'song_title': "U Don't Know", 'id': None}),
("042. Nas - It Ain't Hard to Tell" , {'filename_path': None, 'title': "Nas - It Ain't Hard to Tell", 'track': 42, 'artist': 'Nas', 'year': None, 'qualifier': None, 'song_title': "It Ain't Hard to Tell", 'id': None}),
("043. The Gap Band - Outstanding" , {'filename_path': None, 'title': 'The Gap Band - Outstanding', 'track': 43, 'artist': 'The Gap Band', 'year': None, 'qualifier': None, 'song_title': 'Outstanding', 'id': None}),
("044. Parliament - Give Up The Funk (Tear The Roof Off The Sucker)" , {'filename_path': None, 'title': 'Parliament - Give Up The Funk (Tear The Roof Off The Sucker)', 'track': 44, 'artist': 'Parliament', 'year': None, 'qualifier': 'Tear The Roof Off The Sucker', 'song_title': 'Give Up The Funk', 'id': None}),
("045. The Notorious B.I.G. - Kick in the Door" , {'filename_path': None, 'title': 'The Notorious B.I.G. - Kick in the Door', 'track': 45, 'artist': 'The Notorious B.I.G.', 'year': None, 'qualifier': None, 'song_title': 'Kick in the Door', 'id': None}),
("046. Big Pun - Twinz ft. Fat Joe" , {'filename_path': None, 'title': 'Big Pun - Twinz & Fat Joe', 'track': 46, 'artist': 'Big Pun', 'year': None, 'qualifier': None, 'song_title': 'Twinz & Fat Joe', 'id': None}),
("047. Stevie Wonder - Higher Ground" , {'filename_path': None, 'title': 'Stevie Wonder - Higher Ground', 'track': 47, 'artist': 'Stevie Wonder', 'year': None, 'qualifier': None, 'song_title': 'Higher Ground', 'id': None}),
("048. Common - The 6th Sense ft. Bilal" , {'filename_path': None, 'title': 'Common - The 6th Sense & Bilal', 'track': 48, 'artist': 'Common', 'year': None, 'qualifier': None, 'song_title': 'The 6th Sense & Bilal', 'id': None}),
("049. Raekwon - Incarcerated Scarfaces" , {'filename_path': None, 'title': 'Raekwon - Incarcerated Scarfaces', 'track': 49, 'artist': 'Raekwon', 'year': None, 'qualifier': None, 'song_title': 'Incarcerated Scarfaces', 'id': None}),
("050. A Tribe Called Quest - Award Tour" , {'filename_path': None, 'title': 'A Tribe Called Quest - Award Tour', 'track': 50, 'artist': 'A Tribe Called Quest', 'year': None, 'qualifier': None, 'song_title': 'Award Tour', 'id': None}),
("051. Nas - Nas Is Like" , {'filename_path': None, 'title': 'Nas - Nas Is Like', 'track': 51, 'artist': 'Nas', 'year': None, 'qualifier': None, 'song_title': 'Nas Is Like', 'id': None}),
("052. Nina Simone - Backlash Blues" , {'filename_path': None, 'title': 'Nina Simone - Backlash Blues', 'track': 52, 'artist': 'Nina Simone', 'year': None, 'qualifier': None, 'song_title': 'Backlash Blues', 'id': None}),
("053. Nina Simone - Don't You Pay Them No Mind" , {'filename_path': None, 'title': "Nina Simone - Don't You Pay Them No Mind", 'track': 53, 'artist': 'Nina Simone', 'year': None, 'qualifier': None, 'song_title': "Don't You Pay Them No Mind", 'id': None}),
("054. Nina Simone： Pirate Jenny" , {'filename_path': None, 'title': '054. Nina Simone: Pirate Jenny', 'track': None, 'artist': '054. Nina Simone: Pirate Jenny', 'year': None, 'qualifier': None, 'song_title': '054. Nina Simone: Pirate Jenny', 'id': None}),
("055. Good Girls Don't by THE KNACK" , {'filename_path': None, 'title': "055. Good Girls Don't by THE KNACK", 'track': None, 'artist': "055. Good Girls Don't by THE KNACK", 'year': None, 'qualifier': None, 'song_title': "055. Good Girls Don't by THE KNACK", 'id': None}),
("056. Nina Simone - Mississippi Goddam (Live At Carnegie Hall, New York, 1964 ⧸ Audio)" , {'filename_path': None, 'title': 'Nina Simone - Mississippi Goddam (Live At Carnegie Hall, New York, 1964  Audio)', 'track': 56, 'artist': 'Nina Simone', 'year': None, 'qualifier': 'Live At Carnegie Hall, New York, 1964  Audio', 'song_title': 'Mississippi Goddam', 'id': None}),
("057. ben webster caravan" , {'filename_path': None, 'title': '057. ben webster caravan', 'track': None, 'artist': '057. ben webster caravan', 'year': None, 'qualifier': None, 'song_title': '057. ben webster caravan', 'id': None}),
("058. Nina Simone -  Ain't Got No ⧸ I Got Life (Live 1968)" , {'filename_path': None, 'title': "Nina Simone - Ain't Got No  I Got Life (Live 1968)", 'track': 58, 'artist': 'Nina Simone', 'year': None, 'qualifier': 'Live 1968', 'song_title': "Ain't Got No  I Got Life", 'id': None}),
("059. The Jam   Precious 12 Inch version" , {'filename_path': None, 'title': 'The Jam - Precious 12 Inch version', 'track': 59, 'artist': 'The Jam', 'year': None, 'qualifier': None, 'song_title': 'Precious 12 Inch version', 'id': None}),
("060. Charlie Parker (1946) FIRST RECORDING" , {'filename_path': None, 'title': '060. Charlie Parker (1946) FIRST RECORDING', 'track': None, 'artist': '060. Charlie Parker (1946) FIRST RECORDING', 'year': None, 'qualifier': None, 'song_title': '060. Charlie Parker (1946) FIRST RECORDING', 'id': None}),
("061. NINA SIMONE - Sinnerman (1965)" , {'filename_path': None, 'title': 'NINA SIMONE - Sinnerman (1965)', 'track': 61, 'artist': 'NINA SIMONE', 'year': None, 'qualifier': '1965', 'song_title': 'Sinnerman', 'id': None}),
("062. the clash - train in vain (ext version)" , {'filename_path': None, 'title': 'the clash - train in vain (ext version)', 'track': 62, 'artist': 'the clash', 'year': None, 'qualifier': 'ext version', 'song_title': 'train in vain', 'id': None}),
("063. Nina Simone - I put a spell on you" , {'filename_path': None, 'title': 'Nina Simone - I put a spell on you', 'track': 63, 'artist': 'Nina Simone', 'year': None, 'qualifier': None, 'song_title': 'I put a spell on you', 'id': None}),
("064. Roxy Music - Angel Eyes (1979) full 12” Single" , {'filename_path': None, 'title': 'Roxy Music - Angel Eyes (1979) full 12 Single', 'track': 64, 'artist': 'Roxy Music', 'year': None, 'qualifier': None, 'song_title': 'Angel Eyes (1979) full 12 Single', 'id': None}),
("065. Thelonious Monk - Straight No Chaser 1951" , {'filename_path': None, 'title': 'Thelonious Monk - Straight No Chaser 1951', 'track': 65, 'artist': 'Thelonious Monk', 'year': None, 'qualifier': None, 'song_title': 'Straight No Chaser 1951', 'id': None}),
("066. BIGTOWN PLAYBOY - Eddie Taylor" , {'filename_path': None, 'title': 'BIGTOWN PLAYBOY - Eddie Taylor', 'track': 66, 'artist': 'BIGTOWN PLAYBOY', 'year': None, 'qualifier': None, 'song_title': 'Eddie Taylor', 'id': None}),
("067. Fleetwood Mac - Everywhere (12 Inch Version) 05_47" , {'filename_path': None, 'title': 'Fleetwood Mac - Everywhere (12 Inch Version) 05_47', 'track': 67, 'artist': 'Fleetwood Mac', 'year': None, 'qualifier': None, 'song_title': 'Everywhere (12 Inch Version) 05_47', 'id': None}),
("068. Miles Davis - Freddie Freeloader" , {'filename_path': None, 'title': 'Miles Davis - Freddie Freeloader', 'track': 68, 'artist': 'Miles Davis', 'year': None, 'qualifier': None, 'song_title': 'Freddie Freeloader', 'id': None}),
("069. Nina Simone - To Be Young, Gifted and Black (Live at Philharmonic Hall, New York, NY - October 1969)" , {'filename_path': None, 'title': 'Nina Simone - To Be Young, Gifted & Black (Live at Philharmonic Hall, New York, NY - October 1969)', 'track': 69, 'artist': 'Nina Simone - To Be Young, Gifted & Black (Live at Philharmonic Hall, New York, NY', 'year': None, 'qualifier': None, 'song_title': 'October 1969)', 'id': None}),
("070. Cheap Trick - Surrender. (Guardians of the Galaxy) Vol. 2" , {'filename_path': None, 'title': 'Cheap Trick - Surrender. (Guardians of the Galaxy) Vol. 2', 'track': 70, 'artist': 'Cheap Trick', 'year': None, 'qualifier': None, 'song_title': 'Surrender. (Guardians of the Galaxy) Vol. 2', 'id': None}),
("071. John Coltrane - Naima (Album：Giant Steps) 1959" , {'filename_path': None, 'title': 'John Coltrane - Naima (Album:Giant Steps) 1959', 'track': 71, 'artist': 'John Coltrane', 'year': None, 'qualifier': None, 'song_title': 'Naima (Album:Giant Steps) 1959', 'id': None}),
("072. Nina Simone - Don't Let Me Be Misunderstood" , {'filename_path': None, 'title': "Nina Simone - Don't Let Me Be Misunderstood", 'track': 72, 'artist': 'Nina Simone', 'year': None, 'qualifier': None, 'song_title': "Don't Let Me Be Misunderstood", 'id': None}),
("073. Smokey Smothers - Come on rock little girl" , {'filename_path': None, 'title': 'Smokey Smothers - Come on rock little girl', 'track': 73, 'artist': 'Smokey Smothers', 'year': None, 'qualifier': None, 'song_title': 'Come on rock little girl', 'id': None}),
("074. 1933 HITS ARCHIVE： Sophisticated Lady - Duke Ellington (Brunswick version)" , {'filename_path': None, 'title': '1933 HITS ARCHIVE: Sophisticated Lady - Duke Ellington (Brunswick version)', 'track': 74, 'artist': '1933 HITS ARCHIVE: Sophisticated Lady', 'year': None, 'qualifier': 'Brunswick version', 'song_title': 'Duke Ellington', 'id': None}),
("075. Big Jack  Johnson   Catfish Blues" , {'filename_path': None, 'title': 'Big Jack  Johnson - Catfish Blues', 'track': 75, 'artist': 'Big Jack  Johnson', 'year': None, 'qualifier': None, 'song_title': 'Catfish Blues', 'id': None}),
("076. Blondie - Heart Of Glass (Original 12'' Instrumental Version)" , {'filename_path': None, 'title': 'Blondie - Heart Of Glass (Original 12 Instrumental Version)', 'track': 76, 'artist': 'Blondie', 'year': None, 'qualifier': 'Original 12 Instrumental Version', 'song_title': 'Heart Of Glass', 'id': None}),
("077. Nina Simone - Here Comes the Sun (Audio)" , {'filename_path': None, 'title': 'Nina Simone - Here Comes the Sun (Audio)', 'track': 77, 'artist': 'Nina Simone', 'year': None, 'qualifier': 'Audio', 'song_title': 'Here Comes the Sun', 'id': None}),
("078. Billy ＂The Kid＂ Emerson - Red Hot" , {'filename_path': None, 'title': 'Billy The Kid Emerson - Red Hot', 'track': 78, 'artist': 'Billy The Kid Emerson', 'year': None, 'qualifier': None, 'song_title': 'Red Hot', 'id': None}),
("079. David Bowie - Look Back In Anger" , {'filename_path': None, 'title': 'David Bowie - Look Back In Anger', 'track': 79, 'artist': 'David Bowie', 'year': None, 'qualifier': None, 'song_title': 'Look Back In Anger', 'id': None}),
("080. Miles Davis - A NIGHT IN TUNISIA - Paparelli-Dizzy Gillespie - 1955" , {'filename_path': None, 'title': 'Miles Davis - A NIGHT IN TUNISIA - Paparelli-Dizzy Gillespie - 1955', 'track': 80, 'artist': 'Miles Davis - A NIGHT IN TUNISIA - Paparelli-Dizzy Gillespie', 'year': None, 'qualifier': None, 'song_title': '1955', 'id': None}),
("081. Nina Simone Sunday In Savannah (Live)" , {'filename_path': None, 'title': '081. Nina Simone Sunday In Savannah (Live)', 'track': None, 'artist': '081. Nina Simone Sunday In Savannah (Live)', 'year': None, 'qualifier': None, 'song_title': '081. Nina Simone Sunday In Savannah (Live)', 'id': None}),
("082. Eddie Kirkland - Train Done Gone" , {'filename_path': None, 'title': 'Eddie Kirkland - Train Done Gone', 'track': 82, 'artist': 'Eddie Kirkland', 'year': None, 'qualifier': None, 'song_title': 'Train Done Gone', 'id': None}),
("083. Max Roach Quintet - Bemsha Swing" , {'filename_path': None, 'title': 'Max Roach Quintet - Bemsha Swing', 'track': 83, 'artist': 'Max Roach Quintet', 'year': None, 'qualifier': None, 'song_title': 'Bemsha Swing', 'id': None}),
("084. Pretenders - Brass In Pocket (Extended)" , {'filename_path': None, 'title': 'Pretenders - Brass In Pocket (Extended)', 'track': 84, 'artist': 'Pretenders', 'year': None, 'qualifier': 'Extended', 'song_title': 'Brass In Pocket', 'id': None}),
("085. Blues In The Dark , Little George Smith" , {'filename_path': None, 'title': '085. Blues In The Dark , Little George Smith', 'track': None, 'artist': '085. Blues In The Dark , Little George Smith', 'year': None, 'qualifier': None, 'song_title': '085. Blues In The Dark , Little George Smith', 'id': None}),
("086. Ray Charles - A Fool For You (From ＂Legends of Rock 'N' Roll＂ DVD)" , {'filename_path': None, 'title': "Ray Charles - A Fool For You (From Legends of Rock 'N' Roll DVD)", 'track': 86, 'artist': 'Ray Charles', 'year': None, 'qualifier': "From Legends of Rock 'N' Roll DVD", 'song_title': 'A Fool For You', 'id': None}),
("087. The Stone Roses - Waterfall" , {'filename_path': None, 'title': 'The Stone Roses - Waterfall', 'track': 87, 'artist': 'The Stone Roses', 'year': None, 'qualifier': None, 'song_title': 'Waterfall', 'id': None}),
("088. Happy Mondays - Hallelujah" , {'filename_path': None, 'title': 'Happy Mondays - Hallelujah', 'track': 88, 'artist': 'Happy Mondays', 'year': None, 'qualifier': None, 'song_title': 'Hallelujah', 'id': None}),
("089. Harmonica Hinds - Berlin (1977) Part 1" , {'filename_path': None, 'title': 'Harmonica Hinds - Berlin (1977) Part 1', 'track': 89, 'artist': 'Harmonica Hinds', 'year': None, 'qualifier': None, 'song_title': 'Berlin (1977) Part 1', 'id': None}),
("090. Howlin' Wolf - I Ain't Superstitious (1961)" , {'filename_path': None, 'title': "Howlin' Wolf - I Ain't Superstitious (1961)", 'track': 90, 'artist': "Howlin' Wolf", 'year': None, 'qualifier': '1961', 'song_title': "I Ain't Superstitious", 'id': None}),
("091. The Charlatans - Polar Bear (Remastered)" , {'filename_path': None, 'title': 'The Charlatans - Polar Bear (Remastered)', 'track': 91, 'artist': 'The Charlatans', 'year': None, 'qualifier': 'Remastered', 'song_title': 'Polar Bear', 'id': None}),
("092. Inspiral Carpets - Joe" , {'filename_path': None, 'title': 'Inspiral Carpets - Joe', 'track': 92, 'artist': 'Inspiral Carpets', 'year': None, 'qualifier': None, 'song_title': 'Joe', 'id': None}),
("093. Jerry McCain - That's What They Want" , {'filename_path': None, 'title': "Jerry McCain - That's What They Want", 'track': 93, 'artist': 'Jerry McCain', 'year': None, 'qualifier': None, 'song_title': "That's What They Want", 'id': None}),
("094. Jerry Boogie McCain - I'm A King Bee" , {'filename_path': None, 'title': "Jerry Boogie McCain - I'm A King Bee", 'track': 94, 'artist': 'Jerry Boogie McCain', 'year': None, 'qualifier': None, 'song_title': "I'm A King Bee", 'id': None}),
("095. Mock Turtles - Lay Me Down" , {'filename_path': None, 'title': 'Mock Turtles - Lay Me Down', 'track': 95, 'artist': 'Mock Turtles', 'year': None, 'qualifier': None, 'song_title': 'Lay Me Down', 'id': None}),
("096. Left Hand Frank and his Blues Band, Blues won't let me be" , {'filename_path': None, 'title': "096. Left Hand Frank & his Blues Band, Blues won't let me be", 'track': None, 'artist': "096. Left Hand Frank & his Blues Band, Blues won't let me be", 'year': None, 'qualifier': None, 'song_title': "096. Left Hand Frank & his Blues Band, Blues won't let me be", 'id': None}),
("097. THE FARM 'STEPPIN STONE'" , {'filename_path': None, 'title': "097. THE FARM 'STEPPIN STONE'", 'track': None, 'artist': "097. THE FARM 'STEPPIN STONE'", 'year': None, 'qualifier': None, 'song_title': "097. THE FARM 'STEPPIN STONE'", 'id': None}),
("098. Homesick James,  ＂Set a Date＂ 1965" , {'filename_path': None, 'title': 'Homesick James, - Set a Date 1965', 'track': 98, 'artist': 'Homesick James,', 'year': None, 'qualifier': None, 'song_title': 'Set a Date 1965', 'id': None}),
("099. James - Sometimes" , {'filename_path': None, 'title': 'James - Sometimes', 'track': 99, 'artist': 'James', 'year': None, 'qualifier': None, 'song_title': 'Sometimes', 'id': None}),
("100. John Primer  ~ '' Blue And Lonesome ''  2013" , {'filename_path': None, 'title': 'John Primer  ~ - Blue And Lonesome   2013', 'track': 100, 'artist': 'John Primer  ~', 'year': None, 'qualifier': None, 'song_title': 'Blue And Lonesome   2013', 'id': None}),
("101. Primal Scream - Come Together" , {'filename_path': None, 'title': 'Primal Scream - Come Together', 'track': 101, 'artist': 'Primal Scream', 'year': None, 'qualifier': None, 'song_title': 'Come Together', 'id': None}),
("102. Northside - Take Five" , {'filename_path': None, 'title': 'Northside - Take Five', 'track': 102, 'artist': 'Northside', 'year': None, 'qualifier': None, 'song_title': 'Take Five', 'id': None}),
("103. The Soup Dragons - Divine Thing (Remastered)" , {'filename_path': None, 'title': 'The Soup Dragons - Divine Thing (Remastered)', 'track': 103, 'artist': 'The Soup Dragons', 'year': None, 'qualifier': 'Remastered', 'song_title': 'Divine Thing', 'id': None}),
("104. The Stone Roses - She Bangs the Drums" , {'filename_path': None, 'title': 'The Stone Roses - She Bangs the Drums', 'track': 104, 'artist': 'The Stone Roses', 'year': None, 'qualifier': None, 'song_title': 'She Bangs the Drums', 'id': None}),
("105. Happy Mondays - Loose Fit" , {'filename_path': None, 'title': 'Happy Mondays - Loose Fit', 'track': 105, 'artist': 'Happy Mondays', 'year': None, 'qualifier': None, 'song_title': 'Loose Fit', 'id': None}),
("106. THE CHARLATANS - Indian rope" , {'filename_path': None, 'title': 'THE CHARLATANS - Indian rope', 'track': 106, 'artist': 'THE CHARLATANS', 'year': None, 'qualifier': None, 'song_title': 'Indian rope', 'id': None})]