"""English content of the Keepsight website."""

MAIL = "keepsight.support@gmail.com"
ADDRESS = "Andreas Reinert<br>Heuweg 14<br>4665 Oftringen<br>Switzerland"

UI = {
    "name": "English",
    "nav_home": "Overview",
    "nav_docs": "Documentation",
    "nav_support": "Support",
    "privacy": "Privacy",
    "imprint": "Imprint",
    "language": "Language",
    "prev": "Back",
    "next": "Next",
    "docs_title": "Documentation",
    "docs_lead": "Everything Keepsight can do, explained step by step. The chapters build on each other, but you can start anywhere.",
    "chapters": "Chapters",
}

HOME = {
    "title": "Keepsight: stay in the moment, keep the shot",
    "description": "Make cool videos and memorable snapshots with smart subject tracking and easy controls. Detection runs on your iPhone.",
    "h1": 'Put the iPhone down. Keepsight films you.',
    "lead": 'Stand it on a table, a tripod or a gimbal and step into the picture. Keepsight keeps you in the frame while you move.',
    "cta": "Read the documentation",
    "note": "Keepsight is currently in beta testing and not yet available on the App Store.",
    "how_h": "How it works",
    "how": [
        ('Put it down', 'Lean the iPhone against something, use a tripod or place it in a gimbal.'),
        ('Step into the picture', 'Keepsight recognises you and follows you. Without a gimbal, the frame of the video moves with you.'),
        ('Record and share', 'Press record and share the finished video straight from the app.'),
    ],
    "solo_h": 'No gimbal? No problem.',
    "solo_p": 'Keepsight is a complete camera app even without a gimbal, handheld or on a small tripod. Made for vlogs, selfies and group photos.',
    "solo": [
        ('Auto capture', 'Put the iPhone down and step into the picture. With Keepsight Pro the app takes the photo by itself when everyone smiles or looks at the camera.'),
        ('Dual capture', 'Film what happens in front of you and your own reaction at the same time. With Keepsight Pro your selfie appears as a small picture in the video.'),
        ('Virtual gimbal', 'Without a motor, Keepsight saves a video whose frame follows the subject smoothly, in 2K with Keepsight Pro. It works handheld too.'),
        ('Hands-free', 'Start a video or take a photo with a hand gesture or your voice, with a countdown so everyone is ready.'),
    ],
    "control_h": 'Full control over the camera',
    "control_p": 'With Keepsight Pro you set exposure, ISO, shutter, white balance, tint and focus yourself, each one separately. Whatever you leave alone stays automatic.',
    "sound_h": 'Sound as good as the picture',
    "sound_p": 'Keepsight shows your sound level before and while you record and warns you when you are too quiet, too loud or distorted. With Keepsight Pro you choose the microphone, record your voice through AirPods or a wireless microphone, and capture spatial audio on the iPhone models that support it.',
    "stories_h": "Made for your moments",
    "stories": [
        ("", "Creators and friends", "From your first vlog to spontaneous moments with friends, Keepsight helps keep the action in the frame. Choose what matters, film naturally and make your everyday videos more fun, without turning every shot into a technical project.", "docs/start.html", "Your first tracking"),
        ("story-family", "Families and travel", "The moments worth keeping happen quickly: a family trip, laughter together, a day outside. Keepsight makes videos and spontaneous snapshots easier, so you can stay in the moment while tracking helps with the framing. With Keepsight Pro the app can even take the photo by itself when everyone smiles.", "docs/photo.html", "Photos and triggers"),
        ("story-sport", "Sport and action", "Moving subjects make memorable clips. Follow a cyclist or a runner with a supported gimbal and choose how quickly the camera reacts. How well it works depends on the speed, the distance, the light and your gimbal.", "docs/tracking.html", "Tracking subjects"),
        ("story-pets", "Pets and wildlife", "Pets and wild animals rarely stay still. Keepsight follows moving animals and captures the action. Very fast or erratic birds, however, can be quicker than your gimbal can turn or than the iPhone can recognise them.", "docs/tracking.html#fast", "Fast animals and birds"),
        ("story-pro", "Photo and video enthusiasts", "Get more out of a camera on a gimbal. On a supported DockKit gimbal or the FeiyuTech AK4500, the iPhone works as a smart tracking assistant while your camera keeps recording the actual footage on its own.", "docs/rig.html", "Set up the rig step by step"),
        ("story-aviation", "Plane spotters", "Bring more context to the aircraft you film. Keepsight follows aircraft by sight. With your own local ADS-B receiver it can also add flight data to the iPhone video, in countries where this feature is approved. At present no region is approved.", "docs/flight.html", "Flight data"),
    ],
    "stories_note": "The photos on this page are illustrations. They are not screenshots of the app and no proof of compatible devices.",
    "shots_h": "What the app looks like",
    "what_h": "What Keepsight does for you",
    "what": [
        ("Follow", "Choose a subject: person, face, aircraft, bird, animal, vehicle, train or boat. Keepsight keeps it centred and steers the gimbal. If a cloud hides the aircraft, the app briefly keeps following its path."),
        ("Zoom", "Auto zoom keeps the subject at the size you set. It moves in tiny steps and stays within the selected lens, so the video never jumps."),
        ("Frame", "Without a motor, Keepsight saves a video whose frame follows the subject smoothly, in 2K with Keepsight Pro. It works handheld too."),
        ("Shoot", "With Keepsight Pro the app takes the photo by itself when everyone smiles, when everyone looks at the camera, or when the subject is large enough in the frame. Interval series, hand gestures and voice commands with a countdown are already part of the free version."),
    ],
    "cam_h": "The full camera of your iPhone",
    "cam": [("4K", "Video at 24, 25, 30 or 60 frames per second"),
            ("Up to 48 MP", "Photos, depending on iPhone and lens, as HEIF or ProRAW"),
            ("3", "Lenses: ultra wide, main camera and telephoto")],
    "price_h": 'Filming people is free',
    "price_p": 'Follow people and faces for as long as you like, in 1080p with a small logo. Keepsight Pro is for everyone who wants more quality: 4K without logo, more subjects and the professional tools. One purchase, no subscription.',
    "price_rows": [
        ('Track person and face', True, True),
        ('Unlimited recording in 1080p, with a small logo', True, True),
        ('Auto zoom and virtual gimbal', True, True),
        ('Gimbal control with Apple DockKit', True, True),
        ('Gestures, voice commands, countdown', True, True),
        ('Pro preview: 3 sessions of 3 minutes', True, True),
        ('4K video without logo', False, True),
        ('Aircraft, bird, animal, vehicle, train, boat', False, True),
        ('Drag a frame around any object', False, True),
        ('FeiyuTech AK4500 and manual gimbal control', False, True),
        ('Auto capture: smile, look, subject', False, True),
        ('Manual camera controls for photo and video', False, True),
        ('Focus follows the subject, zebra, peaking, histogram, audio meters, frame guides', False, True),
        ('Sound menu: microphone, headphones, spatial audio', False, True),
        ('Dual capture: video with selfie picture', False, True),
        ('Second video with frames and data', False, True),
        ('Photos in 12 MP', True, True),
        ('Photos up to 48 MP and in ProRAW', False, True),
        ('Video in ProRes 422 HQ', False, True),
        ('Gimbal: framing, speaker and pan programs', False, True),
        ('Gestures: group, framing, highlights, own assignment', False, True),
        ('Heat saver while recording, AF button', True, True),
        ('Apple Watch: shutter, mode, tracking, status', True, True),
        ('Apple Watch: alerts, controls, live view, highlights', False, True),
    ],
    "price_cols": ("Feature", "Free", "Pro"),
    "price_note": 'The free version films people in 1080p with a small Keepsight logo, without a time limit.',
    "free_line": 'Filming people is free and unlimited.',
    "try_h": "Try Keepsight for free",
    "try": [
        'The free version films people in 1080p with a small Keepsight logo, without a time limit.',
        'Pro preview: 3 sessions of 3 minutes. The time only runs while Keepsight follows a subject.',
        "Test your subject and your gimbal before you buy.",
    ],
    "pro_card": 'For more quality: 4K without logo, animals, vehicles and aircraft, and all professional tools. Buy once, no subscription.',
    "campaign": {
        "prelaunch": "Planned for the launch in the Swiss App Store: CHF 15.00 as a one-time purchase.",
        # Nicht mehr verwendet (Stufenpreis verworfen), bleibt für die Nummerierung der Übersetzungen
        "intro": ("Launch price: CHF 14.90 – one-time, no subscription.", "Only until 31 March 2027 inclusive.", "From 1 April 2027: CHF 19.90."),
        "regular": "Keepsight Pro – CHF 15.00 one-time. No subscription.",
        "unverified": "The App Store shows the current price in your currency.",
        "swiss": "Prices in Swiss francs apply to the Swiss App Store. In other countries the App Store shows the price in your currency.",
        "store": "Download on the App Store",
    },
    "faq_h": "Questions and answers",
    "faq": [
        ('Do I need a gimbal?', 'No. Camera, auto capture, dual capture, gestures, voice commands and the virtual gimbal work handheld or on a tripod. A gimbal adds real camera movement.'),
        ("Do I pay once or regularly?", "Once. Keepsight Pro is a one-time purchase, with no subscription and no recurring costs."),
        ("What can I do for free?", 'Follow people and faces without a time limit, with gestures, voice commands, the virtual gimbal and any DockKit gimbal. Videos are saved in 1080p with a small logo. You can also try Pro three times for 3 minutes.'),
        ("How do I restore my purchase?", "In the app, open the Pro screen and choose to restore the purchase. You must be signed in with the Apple Account you bought with."),
        ("Why does the price differ in my country?", "Apple sets the price per country and currency, including taxes. The price shown in your App Store is the one that applies."),
        ("Does Keepsight work without internet?", "Yes. Detection and tracking run on the iPhone. Internet is needed only for the purchase."),
        ("What happens to my pictures?", "They stay on your iPhone. Keepsight has no account, no advertising and no analytics."),
        ("Does Keepsight record with my big camera?", "No. Keepsight steers the gimbal; the camera on it records on its own. Keepsight's own photos and videos come from the iPhone camera."),
        ("Is live flight data available where I live?", "Only in approved countries and regions, and it needs your own ADS-B receiver and location access. At present no region is approved."),
        ("Can Keepsight follow fast birds?", "Not always. Very fast or erratic animals can be quicker than the gimbal can turn or than the iPhone can recognise them."),
    ],
    "need_h": "What you need",
    "need": [
        ("iPhone", "An iPhone with iOS 26 or later. Keepsight is developed and tested on the iPhone 15 Pro Max and iPhone 17 Pro Max with three cameras."),
        ("Gimbal", "For following, a gimbal or stand with Apple DockKit, such as the Insta360 Flow 2 Pro, DJI Osmo Mobile 8 or Belkin Auto-Tracking Stand Pro. The FeiyuTech AK4500 for mirrorless cameras is supported as well. Camera, photo triggers, gestures, voice and the virtual gimbal also work without a gimbal."),
        ("Languages", "The app speaks 21 languages: English, German, French, Italian, Spanish, Portuguese, Dutch, Swedish, Polish, Russian, Ukrainian, Turkish, Arabic, Hindi, Indonesian, Vietnamese, Thai, Japanese, Korean and Chinese (Simplified and Traditional)."),
    ],
}

DOCS = [
("start", "Getting started", "Permissions, connecting the gimbal, your first tracking.", """
<h2>Permissions</h2>
<p>On first launch the iPhone asks for access. Keepsight only asks for each one when it is needed.</p>
<table>
<tr><th>Access</th><th>What for</th></tr>
<tr><td>Camera</td><td>Detecting and filming subjects. The app does not work without the camera.</td></tr>
<tr><td>Bluetooth</td><td>Controlling the gimbal.</td></tr>
<tr><td>Photos</td><td>Saving captures and showing them in the gallery. “Limited access” is enough.</td></tr>
<tr><td>Microphone</td><td>Sound for videos and voice commands.</td></tr>
<tr><td>Speech recognition</td><td>Voice commands only.</td></tr>
<tr><td>Location</td><td>Live flight data only: checking your region and recognising the aircraft. Stays on the iPhone.</td></tr>
<tr><td>Local network</td><td>Live flight data only: connecting to your own ADS-B receiver.</td></tr>
</table>
<p>If you declined an access, you can allow it later under <kbd>Settings</kbd> → <kbd>Keepsight</kbd>.</p>

<h2>Connecting the gimbal</h2>
<ul>
<li><strong>Gimbal or stand with Apple DockKit:</strong> Pair the device with your iPhone once, as the manufacturer describes. After that, Keepsight connects by itself when you mount the iPhone.</li>
<li><strong>FeiyuTech AK4500:</strong> Switch the gimbal on. In the full view, touch and hold the gimbal symbol in the bar at the bottom and choose FeiyuTech AK4500.</li>
</ul>
<p>Once connected, the gimbal symbol turns green. Details are in the chapter <a href="gimbals.html">Supported gimbals</a>.</p>
<div class="tip"><p>The gimbal must be able to turn freely. Keep fingers, cables and objects out of its range of movement.</p></div>

<h2>Your first tracking</h2>
<p>In simple mode there is nothing to set up: step in front of the camera and press record. The steps below are for the full view.</p>
<ol>
<li>Open the left panel and choose the subject <kbd>Person</kbd>.</li>
<li>Step in front of the camera. A frame appears around you and the status at the top left reads “Target locked”.</li>
<li>Tracking is on by default: <kbd>Tracking</kbd> in the bar at the bottom is green and the gimbal follows you. Tap it to switch tracking off; it then turns yellow.</li>
</ol>
<p>If the gimbal turns away from the subject instead of towards it, Keepsight notices it after a moment and reverses the direction by itself. You can also invert an axis under <kbd>All settings</kbd> → <kbd>Direction</kbd>.</p>
"""),

("gimbals", "Supported gimbals", "Which devices Keepsight controls, how to connect them and move them by hand.", """
<p>Keepsight controls gimbals and stands through DockKit, Apple’s interface for motorised mounts. This is the recommended way: devices connect by themselves and Apple looks after the connection. In addition, Keepsight controls the FeiyuTech AK4500 directly over Bluetooth.</p>
<table>
<tr><th>Device</th><th>Connection</th></tr>
<tr><td>Insta360 Flow Pro and Flow 2 Pro</td><td>Apple DockKit</td></tr>
<tr><td>DJI Osmo Mobile 8</td><td>Apple DockKit</td></tr>
<tr><td>Belkin Auto-Tracking Stand Pro</td><td>Apple DockKit</td></tr>
<tr><td>Other devices with DockKit</td><td>Apple DockKit</td></tr>
<tr><td>FeiyuTech AK4500</td><td>Bluetooth, directly from Keepsight</td></tr>
</table>
<div class="tip"><p><strong>Good to know:</strong> The AK4500 has no official interface for third-party apps. Keepsight talks to it through the maker’s Bluetooth protocol. This works, but it can change with new firmware, and some functions of the gimbal are still missing.</p></div>
<p>If a device does not respond as expected, please send a message with the exact model.</p>

<h2>Gimbal with Apple DockKit</h2>
<ol>
<li>Pair the device with your iPhone once. Usually you hold the iPhone against the mount and confirm the request. The manufacturer’s instructions describe the exact steps.</li>
<li>Mount the iPhone and open Keepsight. The app detects the device by itself: the gimbal symbol in the bar at the bottom turns green and reads DockKit.</li>
<li>Choose the subject in Keepsight and tap the tracking button.</li>
</ol>
<p>While Keepsight tracks, it tells DockKit where the subject is, and DockKit moves the motors, as Apple recommends. For Person and Face you can also let Apple’s own tracking take over. If you disconnect in the <kbd>Manual</kbd> area, the system takes over again.</p>
<p>DockKit requires iOS 26 or later. Keepsight cannot control devices without DockKit, such as older models from the same manufacturers.</p>
<h3>Example: DJI Osmo Mobile 8</h3>
<ol>
<li>Update the gimbal’s firmware once with the DJI Mimo app, then close DJI Mimo completely.</li>
<li>Turn on Bluetooth on the iPhone and switch the gimbal on.</li>
<li>Unlock the iPhone and hold it against the NFC area on the handle until the pairing request appears. Confirm it and wait until it shows “Done”. The first preparation can take a while.</li>
<li>Place the iPhone in the holder. Only then does the gimbal connect, and Keepsight shows it as connected.</li>
</ol>
<p>The Bluetooth search in Keepsight is only for the FeiyuTech AK4500. A DockKit gimbal does not appear there; it connects by itself as soon as the iPhone sits in the holder.</p>

<h2>FeiyuTech AK4500</h2>
<ol>
<li>Switch the gimbal on. Close the Feiyu app, because the gimbal accepts only one connection.</li>
<li>Touch and hold the gimbal symbol in the bar at the bottom and choose FeiyuTech AK4500.</li>
<li>Allow Bluetooth access the first time.</li>
</ol>
<p>The AK4500 only reacts above a certain command strength. Keepsight compensates for this with the <kbd>Minimum speed</kbd> setting, see the Settings chapter.</p>

<h2>Buttons on the gimbal</h2>
<p>The buttons of a DockKit gimbal work in Keepsight as in Apple’s Camera app: the shutter button takes a photo or starts and stops a video, the switch button changes between back and front camera, and the zoom wheel zooms in small steps. Auto zoom switches off when you zoom by hand.</p>

<h2>Gimbal settings in the Tracking panel</h2>
<p>You find these under <kbd>Gimbal</kbd> in the Tracking panel. <kbd>Framing</kbd> and <kbd>Search when lost</kbd> work with every gimbal. The other settings appear as soon as a DockKit device is docked, together with its battery level.</p>
<h3>Framing</h3>
<p>Framing: keeps the subject in the left or right third, for example to leave room for text or in the direction it moves. Works with every gimbal.</p>
<h3>Search when lost</h3>
<p>If the subject disappears, the gimbal pans briefly in the direction it left, then to the other side and back. It stops after about 12 seconds.</p>
<h3>Apple-compliant control</h3>
<p>Recommended. Keepsight tells DockKit where the subject is, and DockKit moves the motors, as Apple intends. Off: Keepsight sets the motor speed directly.</p>
<h3>Apple tracking for people</h3>
<p>For Person and Face, Apple's own tracking moves the gimbal, as in the Camera app. Tap a person to choose them. All other subjects stay with Keepsight.</p>
<h3>Follow the speaker</h3>
<p>With several people, the gimbal turns to whoever is speaking, for interviews, podcasts or family rounds. Needs Apple tracking for people and iOS 18.</p>
<h3>Pan range</h3>
<p>Limits how far the gimbal may pan, measured from where it points when tracking starts. Useful on a balcony or when a cable hangs from the iPhone.</p>
<h3>Pan program</h3>
<p>Pans slowly and evenly over the chosen angle and time, for time-lapses, panoramic videos or product shots. In video mode Keepsight records; in photo mode with Interval it takes the series. Tracking pauses meanwhile.</p>
<p>Before the pan starts, the gimbal turns to the starting point, so the recording only begins once it is there. The pan range also applies to the program.</p>
<p><kbd>Framing</kbd>, <kbd>Follow the speaker</kbd> and the pan program are part of Keepsight Pro.</p>
<div class="tip"><p><strong>Not yet tested:</strong> These DockKit functions follow Apple’s documentation but have not yet been tried with a DockKit gimbal. If something behaves differently, please send a message with the exact model.</p></div>

<h2>Moving by hand</h2>
[[shots manual]]
<p>The <kbd>Manual</kbd> area at the bottom of the app is for checking the connection.</p>
<ul>
<li><strong>Joystick:</strong> moves the gimbal left, right, up and down.</li>
<li><strong>Speed:</strong> sets how fast it turns.</li>
<li><strong>Connect and disconnect</strong>, and the current state of the connection.</li>
</ul>
<p>If the gimbal moves the wrong way here, invert the axis under <kbd>All settings</kbd> → <kbd>Direction</kbd>.</p>

<h2>Without a gimbal</h2>
<p>Camera, photos, auto capture, gestures, voice commands and the virtual gimbal also work without a gimbal, handheld or on a tripod.</p>
"""),

("rig", "Filming with the big camera", "The rig Keepsight is meant for: the camera records, the iPhone does the tracking.", """
<p>A strong gimbal carries your mirrorless camera. The iPhone sits on top, looks in the same direction and acts as the eye: it detects the subject and drives the motors. The camera underneath takes the footage, with its sensor, its lenses and its resolution, for example 8K on a Lumix S1RII.</p>
<table>
<tr><th>Part</th><th>Job</th></tr>
<tr><td>Camera</td><td>Records the video or photos you will use later.</td></tr>
<tr><td>iPhone with Keepsight</td><td>Detects the subject, keeps it centred and steers the gimbal.</td></tr>
<tr><td>Gimbal</td><td>Carries both and follows.</td></tr>
</table>

<h2>What you need</h2>
<ul>
<li><strong>A camera gimbal that Keepsight controls.</strong> At present that is the FeiyuTech AK4500. It is rated by its maker for up to 4.6&nbsp;kg. Gimbals with Apple DockKit are built for the iPhone alone and do not carry a camera.</li>
<li><strong>A phone holder</strong> for the camera's hot shoe or a thread on the gimbal. It should tilt and lock firmly.</li>
<li><strong>A camera and lens</strong> that stay below the payload limit together with the iPhone and holder.</li>
</ul>

<h2>Mounting and aligning</h2>
<ol>
<li>Mount the camera with the lens you plan to use and put the iPhone into the holder, rear cameras facing forward.</li>
<li>Balance the gimbal with everything that rides on it, including the iPhone. Switch it on only afterwards.</li>
<li>Point the camera at a distant, distinct point such as the top of a church tower, so that it sits in the centre of the camera's image.</li>
<li>Open Keepsight and adjust the holder until the same point lies on the cross in the middle of the viewfinder. Lock the holder.</li>
<li>Connect the gimbal, see the chapter Supported gimbals.</li>
</ol>
<div class="tip"><p>The iPhone sits a few centimetres above the lens. For distant subjects such as aircraft this does not matter. For subjects a few metres away, the subject appears slightly higher in the camera than in the iPhone. In that case, align on a point at your typical working distance.</p></div>

<h2>Choosing the iPhone lens</h2>
<p>Keepsight keeps the subject in the centre of the iPhone's image. The narrower the iPhone's angle of view, the more precisely the centre is held, and the harder it is for the app to find a subject that is not in the picture yet.</p>
<table>
<tr><th>Focal length on the camera (full frame)</th><th>Lens on the iPhone</th></tr>
<tr><td>Up to about 35 mm</td><td>1× (24 mm)</td></tr>
<tr><td>About 35 to 100 mm</td><td>1× or the telephoto</td></tr>
<tr><td>Above 100 mm</td><td>Telephoto (5× on iPhone 15 Pro Max, 120 mm)</td></tr>
</table>
<p>Leave auto zoom off in this rig. It only changes the iPhone's picture, not the camera's.</p>

<h2>Recording</h2>
<ol>
<li>Choose the subject in Keepsight and tap the tracking button.</li>
<li>Start recording on the camera itself. Keepsight does not trigger the camera.</li>
<li>Set focus and exposure on the camera, ideally with its own subject-detection autofocus.</li>
</ol>
<p>To film with the iPhone as well, press its shutter too. The overlay video with frames and gimbal data is a good way to check afterwards how cleanly the tracking worked.</p>

<h2>Speed with a heavy load</h2>
<ul>
<li>Start with <kbd>Smooth</kbd> or <kbd>Standard</kbd>. A heavy camera keeps swinging longer after hard commands.</li>
<li>For fast subjects such as low-flying aircraft choose <kbd>Sport</kbd> and check that the gimbal stays calm.</li>
<li>If the gimbal swings around the subject, lower the gain under <kbd>Custom</kbd> or widen the calm zone.</li>
<li>The longer the camera's focal length, the more every correction shows in the picture. Long lenses call for a softer setting.</li>
</ul>
"""),

("viewfinder", "The viewfinder", "The controls in the camera image and the three panels.", """
[[shots tracking-help camera format-video]]
<p>The viewfinder shows the camera image with almost no controls. Everything else sits in three panels that you bring in when needed.</p>
<h2>In the viewfinder</h2>
<table>
<tr><th>Element</th><th>Meaning</th></tr>
<tr><td>Status, top left</td><td>Searching, Target locked, Predicting or Target lost. “Detection off” means detection is switched off. A thermometer shows that the iPhone is hot.</td></tr>
<tr><td>Format, top centre</td><td>Current resolution and frame rate, in photo mode file type and megapixels. Tap to open the format panel.</td></tr>
<tr><td>Green frame</td><td>The target Keepsight follows. White frames are other detected subjects.</td></tr>
<tr><td>Lenses</td><td><kbd>.5×</kbd>, <kbd>1×</kbd>, <kbd>5×</kbd> and, in video mode, <kbd>A</kbd> for auto zoom.</td></tr>
<tr><td>Shutter</td><td>Red in video mode, white in photo mode.</td></tr>
<tr><td>Switch on the left</td><td>Changes between video and photo.</td></tr>
<tr><td>Switch camera</td><td>The round button next to the thumbnail changes between rear and front camera.</td></tr>
<tr><td>Thumbnail</td><td>The latest capture. Tap to open the gallery.</td></tr>
<tr><td>Bar at the bottom</td><td>Tracking and gimbal: green is on, yellow is off, a tap switches. Below the gimbal symbol you see what is in use: Virtual, DockKit or Bluetooth.</td></tr>
</table>

<h2>The three panels</h2>
<ul>
<li><strong>Left, Tracking:</strong> subject, speed, gestures, voice control, countdown and the gimbal connection.</li>
<li><strong>Right, Camera:</strong> format, auto zoom, virtual gimbal, photo trigger and overlay video.</li>
<li><strong>Bottom, Format:</strong> resolution and frame rate for video, file type and megapixels for photos.</li>
</ul>
<p>Open the side panels with the narrow handles at the edge of the image, by tapping or swiping. In landscape, the handle for the camera panel is a button at the top of the right column. Tap beside a panel to close it.</p>

<h2>Choosing the target in the image</h2>
<ul>
<li><strong>Tap</strong> a white frame to make that subject the target.</li>
<li><strong>Drag a frame</strong> with your finger to follow any object, even one Keepsight does not know. This requires Keepsight Pro.</li>
</ul>
<p>Keepsight rotates its interface when you turn the iPhone to landscape, even when the orientation lock is on, like Apple’s Camera app. During a video recording the image format stays fixed.</p>
"""),

("tracking", "Tracking subjects", "Subject types, custom target, speed and behaviour when the subject is hidden.", """
[[shots tracking-help tracking]]
<h2>Choosing a subject</h2>
<p>In the left panel you choose what Keepsight should look for.</p>
<table>
<tr><th>Subject</th><th>Version</th><th>Note</th></tr>
<tr><td>Person</td><td>Free</td><td>The whole body. Good for sports and movement.</td></tr>
<tr><td>Face</td><td>Free</td><td>For close-ups, vlogs and selfies. Keepsight aims at the eyes: the eye line sits in the centre of the picture, not the nose.</td></tr>
<tr><td>Aircraft</td><td>Pro</td><td>Works best in the sky with the telephoto lens.</td></tr>
<tr><td>Bird</td><td>Pro</td><td></td></tr>
<tr><td>Animal</td><td>Pro</td><td>Dogs, cats, horses and more.</td></tr>
<tr><td>Vehicle</td><td>Pro</td><td>Cars, motorcycles, buses, trucks.</td></tr>
<tr><td>Train</td><td>Pro</td><td></td></tr>
<tr><td>Boat</td><td>Pro</td><td></td></tr>
</table>
<p>If several matching subjects are in the image, Keepsight takes the one nearest the centre. Tap another frame to switch.</p>

<h2>Switching detection on and off</h2>
<p>Detection takes computing power and warms the iPhone. Keepsight therefore only computes as much as needed:</p>
<ul>
<li><strong>Full rate:</strong> as long as tracking, auto zoom, the virtual gimbal, auto capture, gestures or a custom target need detection.</li>
<li><strong>Preview:</strong> otherwise about five frames per second, so that you see the frames and can choose a target.</li>
<li><strong>Off:</strong> the <kbd>Detection</kbd> switch at the top of the tracking panel turns it off completely. It starts by itself as soon as one of the functions above needs it.</li>
</ul>
<p>The green frame always stays inside the visible picture, even when the subject is larger than the view.</p>

<h2>Custom target</h2>
<p>If you drag a frame around an object, Keepsight follows exactly that object, whatever the subject type. The left panel then shows the button <kbd>Custom target</kbd>. Tap it to clear the selection.</p>

<h2>Speed</h2>
<table>
<tr><th>Profile</th><th>Behaviour</th></tr>
<tr><td>Smooth</td><td>Gentle start, half the top speed, small movements are ignored. For calm footage.</td></tr>
<tr><td>Standard</td><td>Balanced. The right start for most subjects.</td></tr>
<tr><td>Sport</td><td>Reacts fastest. For quick changes of direction.</td></tr>
<tr><td>Custom</td><td>You set all controller values yourself, see the Settings chapter.</td></tr>
</table>

<h2>When the subject disappears</h2>
<ul>
<li><strong>Predicting:</strong> If the subject is hidden briefly, the gimbal keeps panning in the same direction. You set the duration under <kbd>All settings</kbd>; the default is 1.5 seconds.</li>
<li><strong>Target lost:</strong> After that the gimbal stops until the subject is detected again.</li>
</ul>

<h2 id="fast">Fast animals and birds</h2>
[[wide story-birds]]
<p>Very fast or erratic animals, especially small, fast birds, cannot always be followed reliably.</p>
<p>How well tracking works depends on how fast the subject moves across the picture, on its distance and size, on the light and on how steadily the iPhone recognises it. Above all it depends on your gimbal: its highest pan and tilt speed, its acceleration and its delay.</p>
<p>The <kbd>Sport</kbd> speed cannot push a gimbal beyond its mechanical limits. Without a gimbal only the virtual gimbal follows, inside the picture the camera already sees.</p>
<ul>
<li>Keep more distance or zoom out: the subject then crosses the picture more slowly.</li>
<li>Choose <kbd>Sport</kbd> for quick changes of direction.</li>
<li>Good light and a calm background help the detection.</li>
</ul>
"""),

("camera", "Camera and format", "Video and photo mode, resolution, frame rate, lenses.", """
[[shots format-video format-photo]]
<h2>Video or photo</h2>
<p>The switch to the left of the shutter changes the mode. The camera reconfigures itself, as in Apple’s Camera app.</p>
<ul>
<li><strong>Video mode:</strong> continuous zoom across all three lenses, and auto zoom.</li>
<li><strong>Photo mode:</strong> the full photo resolution of the selected lens. The viewfinder image is 4:3.</li>
</ul>

<h2>Setting the format</h2>
<p>Tap the format display at the top centre. The panel is locked during a recording.</p>
<h3>Video</h3>
<table>
<tr><th>Setting</th><th>Options</th></tr>
<tr><td>Resolution</td><td>HD (1920 × 1080) or 4K (3840 × 2160)</td></tr>
<tr><td>Frame rate</td><td>24, 30 or 60 frames per second, 25 for PAL</td></tr>
<tr><td>Codec</td><td>HEVC; ProRes 422 HQ with Keepsight Pro</td></tr>
<tr><td>Controls</td><td><kbd>Auto</kbd> <kbd>Pro</kbd></td></tr>
<tr><td>Grid</td><td><kbd>Off</kbd> <kbd>On</kbd></td></tr>
</table>
<h3>Photo</h3>
<table>
<tr><th>Setting</th><th>Options</th></tr>
<tr><td>Format</td><td>HEIF or RAW (Apple ProRAW, with Keepsight Pro)</td></tr>
<tr><td>Resolution</td><td>Whatever the lens delivers, see below</td></tr>
<tr><td>Controls</td><td><kbd>Auto</kbd> <kbd>Pro</kbd></td></tr>
<tr><td>Grid</td><td><kbd>Off</kbd> <kbd>On</kbd></td></tr>
</table>

<h2 id="manual">Manual controls</h2>
<p>Manual controls: set ISO, shutter, white balance, tint and focus yourself, each one separately. Requires Keepsight Pro.</p>
[[shots pro-exposure pro-aperture]]
<p>To open them, tap the format display at the top and switch <kbd>Controls</kbd> to <kbd>Pro</kbd>. You also find <kbd>Manual controls</kbd> in the camera panel; from there it also works while a video is recording.</p>
<p>The window is low and does not darken the picture, so you see every change at once. A small “A” marks each value the camera still sets itself. As soon as you move a slider, that value is fixed. <kbd>Auto</kbd> hands it back to the camera, <kbd>All auto</kbd> resets everything. Your values apply to photo and video and are kept until you change them.</p>
<div class="tip"><p>New to this? Leave everything on Auto and try Exposure first. Every setting stays automatic until you move its slider. Auto hands it back to the camera.</p></div>
<h3>Exposure</h3>
<p>Exposure: makes the whole picture brighter or darker while the camera keeps measuring the light itself. The easiest control to start with.</p>
<p>Use it when the picture comes out too dark or too bright, for example a subject against a bright sky, snow or a stage. Plus makes it brighter, minus darker, in thirds of a stop from −3 to +3. It also works while ISO or shutter are fixed.</p>
<h3>ISO</h3>
<p>ISO: how sensitive the sensor is. A higher value makes the picture brighter but grainier. Keep it as low as the light allows.</p>
<p>Choose a low ISO in daylight for the cleanest picture and raise it indoors or at dusk. If you fix only the ISO, Keepsight adjusts the shutter time by itself so that the brightness stays right.</p>
<h3>Shutter</h3>
<p>Shutter: how long each picture is exposed. Short times such as 1/1000 freeze fast movement. Longer times let in more light but blur movement.</p>
<p>Use 1/1000 or shorter for birds, sport and aircraft so that they stay sharp. For natural-looking video, use about twice the frame rate, for example 1/60 at 30 frames per second. If you fix only the shutter, Keepsight adjusts the ISO by itself. In video the time cannot be longer than one frame; in photo mode it goes up to 1/4 second.</p>
<h3>White balance</h3>
<p>White balance: matches the colours to the light so that white looks white. Tap the symbol for lamp light, sun, cloud or shade, or set the value in Kelvin.</p>
<p>Fix it when the colours change during a recording, for example when the camera pans from sun into shade, or when lamp light looks too yellow. The symbols set 3200 K for light bulbs, 4000 K for fluorescent light, 5600 K for sun, 6500 K for a cloudy sky and 7500 K for shade. The slider covers 2500 K to 10000 K.</p>
<h3>Tint</h3>
<p>Tint: shifts the colours between green and magenta. Usually only needed under artificial light.</p>
<p>Use it when skin or white walls look greenish or pinkish, which often happens under LED or fluorescent lamps. Move the slider until white looks neutral again. While white balance is fixed and tint is on Auto, tint keeps the value measured last, and the other way round.</p>
<h3>Focus</h3>
<p>Focus: sets the distance that is sharp, from near on the left to far on the right.</p>
<p>Use it when the autofocus hunts, for example through a fence, a window or branches, or with a small subject against the sky. Set the distance once and it stays there. Distant subjects such as aircraft are at the right end of the slider.</p>
<h3>Aperture</h3>
<p>Aperture: the opening of the lens. Keepsight shows the value but cannot change it yet, not even on the iPhone 18 Pro.</p>
<h2 id="grid">Grid</h2>
<p>Grid: two lines each way help you keep the horizon level and place your subject. They are not saved in photos or videos.</p>
<p>Switch it on in the format panel under <kbd>Grid</kbd>. It is available to everyone, also without Pro. Place your subject on one of the four crossing points for a balanced picture, and use the lines to keep the horizon and buildings straight.</p>
<h2 id="af">Focus: AF and following focus</h2>
<p>AF: the button <kbd>AF</kbd> at the end of the lens bar focuses once on the tracked subject, or on the centre of the picture when nothing is tracked. Free for everyone.</p>
<p>Light: the flashlight symbol at the end of the lens bar switches on a light with three brightness levels; a fourth tap switches it off. With the rear camera the light of the iPhone shines. With the front camera a bright border on the screen lights your face; it never appears in the video. If the iPhone gets too warm, iOS switches the light off. Free for everyone.</p>
<p>Tap to focus: tap anywhere in the viewfinder. Keepsight focuses and exposes there once, shown by a yellow square, and selects the subject you tapped. If you set focus or exposure by hand, that setting stays. Free for everyone.</p>
<p>Focus follows the subject: while Keepsight tracks a subject, the focus stays on it, even when it moves to the edge of the picture. Switch it on in the settings under <kbd>Monitoring</kbd> → <kbd>Focus follows the subject</kbd>. It is paused as soon as you set the focus by hand. Requires Keepsight Pro.</p>
<h2 id="monitoring">Monitoring tools</h2>
<p>Monitoring tools show you what the picture really looks like, the way professional cameras do. They appear only on the screen and are never saved in photos or videos. Requires Keepsight Pro.</p>
<p>Quick switches: open the camera menu with the round button on the right. Under <kbd>Monitoring</kbd> you switch each tool on and off with one tap. Tap the frame tile again to change the format.</p>
<table>
<tr><th>Tool</th><th>What it shows</th></tr>
<tr><td><kbd>Zebra</kbd></td><td>White diagonal stripes on areas that are too bright and lose detail. Set the threshold with <kbd>Zebra level</kbd>, from 75 to 100 %. If you see stripes on a face or the sky, lower the exposure.</td></tr>
<tr><td><kbd>Focus peaking</kbd></td><td>Colours the edges that are sharp. Useful with manual focus: turn the focus until your subject lights up. Choose the colour that stands out best: green, red, blue or yellow.</td></tr>
<tr><td><kbd>Histogram</kbd></td><td>How the brightness is spread, from dark on the left to bright on the right. A mountain pressed against the right edge means overexposure, against the left edge underexposure.</td></tr>
<tr><td><kbd>Audio meters</kbd></td><td>Audio tile: shows the sound level while you speak, even before recording. Green is good, yellow is strong, red is too loud. A warning appears when the sound is too quiet, too loud or distorted. The display never appears in the video.</td></tr>
<tr><td><kbd>Frame guide</kbd></td><td>Darkens everything outside the chosen format: 9:16 for Reels and Shorts, 4:5 and 1:1 for posts, 4:3, 16:9, and the cinema formats 1.85:1 and 2.39:1. The video itself keeps its full format, so you can crop it later.</td></tr>
</table>
<h2 id="sound">Sound</h2>
<p>Good sound matters as much as a good picture, especially when you talk to the camera. To open the sound menu, tap the level meter in the viewfinder, or open the camera menu and tap <kbd>Microphone</kbd> under <kbd>Sound</kbd>. It is available in video mode and requires Keepsight Pro. The menu shows only what is possible right now: the AirPods switch appears when Bluetooth headphones are connected, spatial audio only on an iPhone that can record it.</p>
[[shots sound]]
<table>
<tr><th>Setting</th><th>Meaning</th></tr>
<tr><td><kbd>Microphone</kbd></td><td>Shows every microphone the iPhone can use right now, for example headphones or a wireless microphone on the USB-C port.</td></tr>
<tr><td><kbd>Headphones as microphone</kbd></td><td>Records your voice with the microphone of your headphones instead of the iPhone. Good when you stand far from the iPhone. Needs AirPods Pro 2, AirPods 4 or newer; without suitable headphones the switch turns itself off.</td></tr>
<tr><td><kbd>Spatial audio</kbd></td><td>Records the sound in 3D. Afterwards you can separate voice and background in Photos with Audio Mix. Needs an iPhone 16 or later and the built-in microphones.</td></tr>
</table>
<p>Wireless microphones with a USB-C receiver, for example from DJI or Rode, work like any external microphone: plug in the receiver and choose it under <kbd>Microphone</kbd>.</p>
<p>High quality with <kbd>Headphones as microphone</kbd> needs iOS 26 and AirPods with the H2 chip, for example AirPods Pro 2 or AirPods 4. With other Bluetooth headphones, such as older AirPods or Beats, the switch may turn itself off. While it is on, the menu shows the name of the headphones. Spatial audio and headphones as microphone cannot be used together. The overlay video and the virtual gimbal video keep normal stereo sound.</p>
<h2 id="dual">Dual capture: video with selfie picture</h2>
<p>Dual capture: the rear camera films and tracks your subject, the front camera films you at the same time. Your selfie appears as a small picture at the bottom right of the video.</p>
<p>Switch it on in video mode with the <kbd>Dual</kbd> tile in the Camera panel. With <kbd>Save selfie video separately</kbd> in the settings your selfie is also saved as its own video, so you can edit it yourself later. While dual capture is on, the viewfinder shows your selfie at the top right, in landscape at the bottom left.</p>
<ul>
<li>Both cameras record at up to 1080p with 30 frames per second, without 4K or ProRes. The rear camera uses the main lens, zoom is digital.</li>
<li>Tracking, gestures, voice commands and the gimbal keep working.</li>
<li>Only in video mode. In photo mode dual capture pauses and comes back when you return to video mode. Switching to the front camera ends it.</li>
<li>If the iPhone gets hot, the selfie picture switches off by itself.</li>
<li>Requires Keepsight Pro and an iPhone that can film with both cameras at once. If yours cannot, Keepsight tells you.</li>
</ul>
<h2 id="heat">Heat saver while recording</h2>
<p>Long recordings in the sun make every iPhone warm. With <kbd>Save heat while recording</kbd> Keepsight saves energy during a recording and gives everything back when you stop. It is on by default and free for everyone.</p>
<ul>
<li>The screen dims after 10 seconds. Tap it to wake it. The recording continues. To see the picture all the time, for example at a concert, switch off <kbd>Dim screen while recording</kbd> under <kbd>All settings</kbd>.</li>
<li>While your subject stands still, detection runs less often. As soon as it moves, it runs at full speed again.</li>
<li>Gestures are checked less often, voice control stays on.</li>
<li>Monitoring tools and the live view on the Apple Watch update less often.</li>
</ul>
<p>If the iPhone gets warm anyway, Keepsight goes one step further: first the selfie picture switches off, then the overlay video pauses, then detection slows down. When the iPhone is too hot, tracking stops and the recording is saved.</p>
<h2>Front camera and selfies</h2>
<p>The button with the two arrows next to the thumbnail switches to the front camera. You see yourself mirrored, as in Apple’s Camera app. Captures are saved unmirrored, the way others see you; for photos you can change that.</p>
<ul>
<li><strong>Video and photo:</strong> video up to 4K, photos at the full resolution of the front camera.</li>
<li><strong>Subject:</strong> when you switch, Keepsight changes to <kbd>Face</kbd> and aims at your eyes. With a gimbal it follows you in front of the front camera too.</li>
<li><strong>Selfie bar in photo mode:</strong> above the shutter you choose <kbd>Single</kbd>, <kbd>Smile</kbd> or <kbd>Look</kbd>. Smile and Look are armed as soon as you tap them: Keepsight takes the photo by itself when everyone smiles or looks at the camera. Both are part of Keepsight Pro.</li>
<li><strong>Countdown:</strong> with the front camera the screen flashes instead of the light.</li>
<li><strong>Not available:</strong> lens selection and auto zoom, because the front camera has a single lens.</li>
</ul>

<h3>Portrait</h3>
<p><kbd>Portrait</kbd> in the selfie bar or in the camera panel is part of Keepsight Pro.</p>
<ul>
<li><strong>Photo:</strong> Keepsight saves the picture with the front camera’s depth data. Afterwards you adjust the background blur in the Photos app. Portrait photos are HEIF at 12 MP; ProRAW is not possible here.</li>
<li><strong>Video:</strong> Keepsight chooses a format that supports Apple’s Portrait effect, usually 1080p at 30 frames. You switch the effect itself on in Control Center under <kbd>Video effects</kbd>; Keepsight opens it for you. Depending on your iPhone you also find Studio Light and Center Stage there.</li>
</ul>
<p><kbd>Mirror selfies</kbd> in the camera panel saves selfie photos the way you see yourself in the viewfinder.</p>
<p>The camera cannot be switched during a video recording.</p>

<h2>Lenses and megapixels</h2>
<table>
<tr><th>Lens</th><th>Photo resolution</th></tr>
<tr><td><kbd>.5×</kbd> ultra wide</td><td>12 MP; up to 48 MP from iPhone 16 Pro</td></tr>
<tr><td><kbd>1×</kbd> main camera</td><td>12, 24 or 48 MP; in RAW 12 or 48 MP</td></tr>
<tr><td>Telephoto</td><td>12 MP; up to 48 MP from iPhone 17 Pro</td></tr>
</table>
<p>These are Apple’s specifications for the Pro models from iPhone 15 Pro. Keepsight has only been tested on the iPhone 15 Pro Max and iPhone 17 Pro Max so far. Other models deliver fewer megapixels with some lenses. The format panel only ever shows what the current lens of your iPhone really delivers.</p>
<div class="tip"><p>Triggered by voice, Keepsight switches to photo or video mode by itself; gestures work in the mode that is set. Only a photo taken while a video is recording stays at about 10 MP.</p></div>
"""),

("zoom", "Auto zoom", "Keeps the subject at the same size without the video jumping.", """
<p>Auto zoom keeps the subject at the size you set. If it moves away, the camera slowly zooms in. If it comes closer, the camera zooms out.</p>
<h2>Turning it on</h2>
<ol>
<li>Switch to video mode.</li>
<li>Select the lens whose range should be used.</li>
<li>Tap <kbd>A</kbd>. The button shows the current zoom, for example “A 2.3×”.</li>
</ol>

<h2>Why the video does not jump</h2>
<p>When an iPhone camera changes lenses while zooming, the image shifts visibly. Auto zoom therefore stays on the selected lens and moves only minimally with every single frame.</p>
<table>
<tr><th>Selected lens</th><th>Zoom range</th></tr>
<tr><td><kbd>.5×</kbd></td><td>0.5× to just under 1×</td></tr>
<tr><td><kbd>1×</kbd></td><td>1× to just under 4×</td></tr>
<tr><td><kbd>5×</kbd></td><td>5× to 10×</td></tr>
</table>

<h2>Settings</h2>
<ul>
<li><strong>Subject size:</strong> how much of the image the subject should fill, 15 to 60 percent.</li>
<li><strong>Zoom speed:</strong> how fast the zoom may move, 8 to 60 percent per second. Small values look calmer.</li>
</ul>

<h2>Behaviour in special cases</h2>
<ul>
<li>Zooming only starts once the subject has been detected steadily for just under a second.</li>
<li>If the subject reaches the edge of the image, the camera zooms out instead of in.</li>
<li>If the subject is hidden briefly, the zoom holds. Only after one and a half seconds without a subject does it slowly return.</li>
</ul>
"""),

("virtual-gimbal", "Virtual gimbal", "A smoothly following frame, in 2K with Keepsight Pro.", """
<p>The virtual gimbal cuts a frame out of the full camera image that follows the subject. The frame keeps its size, so the picture stays calm. The video is finished right after recording.</p>
<h2>Turning it on</h2>
<ol>
<li>Tap the gimbal symbol in the bar at the bottom until it is green and reads Virtual.</li>
<li>Choose a subject. In the viewfinder you see the frame as a bright outline; the area outside is dimmed.</li>
<li>Start recording.</li>
</ol>
<p>A real gimbal is not needed. You can hold the iPhone in your hand or put it on a tripod. As soon as a gimbal is connected, the virtual gimbal rests: the gimbal follows and the full image is saved.</p>

<h2>Settings</h2>
<table>
<tr><th>Control</th><th>Effect</th></tr>
<tr><td><kbd>Smooth</kbd>, <kbd>Standard</kbd>, <kbd>Sport</kbd></td><td>How quickly the frame follows, in the right panel of the full view.</td></tr>
<tr><td>Also save original</td><td>Saves the full video alongside the framed one.</td></tr>
</table>

<h2>What is saved</h2>
<ul>
<li>The framed video: in 2K (2560 × 1440) with Keepsight Pro when you record in 4K, otherwise in 1080p.</li>
<li>Optionally the original in the selected resolution.</li>
</ul>
<p>If Keepsight loses the subject, the frame slowly returns to the centre. If the subject no longer fits, the frame opens up.</p>
<div class="tip"><p>The virtual gimbal suits little movement, such as vlogs, cooking or training on the spot. If you walk around the room, use a gimbal.</p></div>
<h2>Image stabilization</h2>
<p>Keepsight uses the image stabilization of iOS for videos: a stronger level with the virtual gimbal, the standard level otherwise. You can switch it off under <kbd>All settings</kbd>.</p>
"""),

("photo", "Photos and triggers", "Single shot, interval series and automatic capture at the right moment.", """
[[shots camera camera-zoom]]
<p>In photo mode, the right panel under <kbd>Photo trigger</kbd> sets how Keepsight takes pictures.</p>
<table>
<tr><th>Type</th><th>What happens</th></tr>
<tr><td>Single</td><td>One photo per press of the shutter.</td></tr>
<tr><td>Interval</td><td>A series at a fixed interval until the maximum number is reached.</td></tr>
<tr><td>Smile (Pro)</td><td>Fires when all faces in the image are smiling with open eyes.</td></tr>
<tr><td>Look (Pro)</td><td>Fires when everyone is facing the camera.</td></tr>
<tr><td>Subject (Pro)</td><td>Fires when the selected subject is locked and large enough in the frame.</td></tr>
</table>
<p>Single shot and interval are part of the free version. The three automatic types need Keepsight Pro; in the free version they show a lock.</p>

<h2>Running a series</h2>
<ol>
<li>Choose the trigger type.</li>
<li>Set <kbd>Interval</kbd> and <kbd>Maximum photos</kbd>.</li>
<li>Press the shutter. With the automatic types Keepsight is now armed and waits for the moment.</li>
<li>The display at the top centre counts along, for example “3 / 30”. A second press of the shutter ends the series.</li>
</ol>
<ul>
<li><strong>Interval:</strong> 1 to 30 seconds. With the automatic types it is the minimum gap between two photos.</li>
<li><strong>Maximum photos:</strong> 2 to 100.</li>
</ul>
<div class="tip"><p>For birds and other animals, “Subject” with a short interval works well: Keepsight shoots as soon as the animal is large in the frame and keeps taking pictures while it stays there. The app does not detect where an animal is looking.</p></div>
<p>Photos in 48 MP and ProRAW take longer to save. With a very short interval the actual gap can therefore be longer.</p>
"""),

("remote", "Gestures, voice, countdown", "Operating the camera when you are in front of it yourself.", """
<p>You find all three in the left panel under <kbd>Remote control</kbd>.</p>
<h2>Hand gestures</h2>
<p>Gestures work when the subject is set to Person or Face. Hold a gesture still for about half a second; a bar with the gesture’s icon fills at the top centre. Only the tracked person can give gestures, or without tracking the largest person in the picture. After a gesture, the next one is ignored for 2 seconds.</p>
<p>Keepsight understands five gestures. The first three are the same as on the DJI Osmo Mobile 8, the group gesture is the same as on the Insta360 Flow 2 Pro, and the highlight exists only in Keepsight.</p>
<table>
<tr><th></th><th>Gesture</th><th>Effect</th><th>Version</th></tr>
<tr><td class="gi">✋</td><td>Open hand</td><td>Start or stop tracking the person showing it.</td><td>Free</td></tr>
<tr><td class="gi">✌️</td><td>V sign</td><td>Photo mode: take a photo. Video mode: start or stop the recording.</td><td>Free</td></tr>
<tr><td class="gi">⌜⌟</td><td>Double L with both hands (a frame), shown twice</td><td>Adjust the framing: centre the person and set auto zoom to the size of the frame.</td><td>Pro</td></tr>
<tr><td class="gi">☝️</td><td>Index finger up</td><td>Whole group: everyone in the picture stays in view. Show it again to go back to the person showing it.</td><td>Pro</td></tr>
<tr><td class="gi">👍</td><td>Thumbs up</td><td>Highlight: marks the current moment in the running recording.</td><td>Pro</td></tr>
</table>
<p>The V sign works in the mode that is set. To switch between photo and video hands-free, use a voice command.</p>
<h3>What a highlight is</h3>
<p>A highlight is a bookmark in the video. While a video is recording, show 👍 or tap the star on the Apple Watch, and Keepsight remembers that moment. Later, open the video in Keepsight’s gallery: the marks appear under the video as stars with the time, for example ★ 2:14. Tap one and the video jumps there, one second earlier so you do not miss the start.</p>
<p>Example: you film 20 minutes of training and the best jump is at 7:40. Show 👍 at that moment and find it again later with one tap.</p>
<p>The marks are shown only in Keepsight’s gallery, not in the Photos app or in editing programs, because they are stored in Keepsight and not in the video file. If you delete Keepsight, the marks are gone; the videos stay in Photos.</p>
<h3>Keeping a group in the picture</h3>
<p>☝️ draws one frame around everyone in the picture. Tracking and auto zoom keep the whole group in view, for example for a family, a band or a team. Show ☝️ again and Keepsight follows only the person showing it.</p>
<h3>Handing over</h3>
<p>Stop tracking with ✋ and for about five seconds anyone else can take over with ✋. Useful for interviews or when people take turns in front of the camera.</p>
<h3>Gestures from further away</h3>
<p>When the person giving gestures is small in the picture, Keepsight looks for hands only around that person. The hands then appear larger to the detection, so gestures also work from further away. How far depends on light and lens; this is still being measured.</p>
<h3>Your own assignment</h3>
<p>With Keepsight Pro you can give each gesture a different action in the settings, for example ✌️ always takes a photo, or a gesture does nothing. Reset gestures restores the standard.</p>
<h3>Confirmation</h3>
<p>Keepsight confirms every recognised gesture with the bar in the viewfinder, light and sound. If you wear an Apple Watch with Keepsight, it taps your wrist, so you know even with your back to the iPhone. The watch also has a page with all gestures.</p>

<h2>Voice commands</h2>
<p>Switch on <kbd>Voice control</kbd> and allow the microphone and speech recognition. Speak the commands in the app’s language.</p>
<table>
<tr><th>You say</th><th>Effect</th></tr>
<tr><td>“Take a photo”</td><td>Take a photo.</td></tr>
<tr><td>“Start video” or “Start recording”</td><td>Start video recording.</td></tr>
<tr><td>“Stop”</td><td>End the recording, the series or a running countdown.</td></tr>
</table>
<p>Photo and video need at least two words, for example “make a video”, “start filming”, “take a picture” or “snap a photo”. A single word on its own triggers nothing, so normal conversation does not set off the camera. A single “stop” works only while a recording, a series or a countdown is running. If the camera is in the other mode, Keepsight switches by itself before it triggers.</p>
<p>While voice control is on, the microphone stays active. The iPhone shows this with the orange dot.</p>

<h2>Countdown, flash and sound</h2>
<p>When you trigger by gesture or voice, a countdown runs first so you can get into position.</p>
<ul>
<li><strong>Countdown:</strong> off, 3, 5 or 10 seconds. The seconds are shown large in the image.</li>
<li><strong>Confirmation flash:</strong> the LED blinks at ever shorter intervals until the shot.</li>
<li><strong>Confirmation sound:</strong> a short tick with every flash.</li>
</ul>
<p>Without a countdown there is a single flash and tick as confirmation. The on-screen shutter always fires immediately.</p>
"""),

("watch", "Apple Watch", "Remote control and status on your wrist.", """
<h2>What the watch does</h2>
<p>The Apple Watch is a remote control and status display for the iPhone on the gimbal. It has no camera of its own, shows no gallery and stores nothing.</p>
<p>Open Keepsight on the iPhone, then on the watch. The watch reaches the iPhone over Bluetooth at about 10 m, further on the same Wi-Fi. Without a connection it says so instead of showing empty buttons.</p>
<h2>Free</h2>
<ul>
<li>Shutter: photo, or start and stop video, with the countdown ticking on your wrist.</li>
<li>Switch between photo and video, start and stop tracking.</li>
<li>Status: mode, recording time in red, tracking state, gimbal and its battery.</li>
<li>Gestures page: all hand gestures at a glance. The watch taps your wrist whenever the iPhone recognises a gesture.</li>
<li>Double tap (watchOS 11 or later, Apple Watch Series 9, Ultra 2 or newer) triggers the shutter. On Apple Watch Ultra, set the Action button to Shortcut and choose Keepsight shutter.</li>
</ul>
<h2>With Keepsight Pro</h2>
<ul>
<li>Alerts on your wrist: target lost for 2 seconds, recording stopped, iPhone storage almost full, iPhone hot, gimbal battery low, gimbal disconnected.</li>
<li>Controls: zoom with the Digital Crown, pan and tilt with your finger, centre, next subject, whole group, pan program.</li>
<li>Highlights: a tap during recording marks the moment. In the gallery the marks appear as stars under the video; a tap jumps there.</li>
<li>Live view: a small picture with the detection frames, about 5 to 8 images per second. Tap a person to select the target. It is for checking, not filming, and switches off when the iPhone is hot.</li>
</ul>
<p>One purchase unlocks everything: Keepsight Pro on the iPhone also unlocks the watch. The Pro preview unlocks the watch for its duration too.</p>
<h2>Requirements</h2>
<p>Apple Watch with watchOS 10 or later, paired with an iPhone with iOS 26 or later. Keepsight installs on the watch together with the iPhone app.</p>
<div class="tip"><p><strong>Not yet tested on a watch:</strong> The watch app follows Apple’s documentation. Double tap, the Action button and the live view still need to be tried on real watches.</p></div>
"""),

("recording", "Recording and gallery", "Which videos are created, where they are and how to view them.", """
<h2>Recording video</h2>
<p>In video mode the red shutter starts and stops the recording. The running time appears at the top centre in a red field, in place of the format. Videos have sound and are saved to the Photos app.</p>

<h2>Which videos are created</h2>
<table>
<tr><th>Video</th><th>Content</th><th>When</th></tr>
<tr><td>Original</td><td>The clean camera image in the selected resolution.</td><td>Without the virtual gimbal always. With it only if <kbd>Also save original</kbd> is on.</td></tr>
<tr><td>Virtual gimbal</td><td>The following frame, in 2K with Keepsight Pro, otherwise in 1080p.</td><td>When the virtual gimbal is on.</td></tr>
<tr><td>Overlay video</td><td>The image with frames, time, subject, status and gimbal data in 1080p.</td><td>With Keepsight Pro, when <kbd>Overlay video</kbd> is on.</td></tr>
</table>

<h2>Gallery</h2>
<p>The thumbnail above the mode switch shows the latest capture. Tap it to open the gallery with all photos and videos you made with Keepsight, newest first.</p>
<p>After a photo the viewfinder darkens briefly and the new picture jumps into the thumbnail. A message only appears if something goes wrong.</p>
<p>Videos with highlights show stars with the time under the video; a tap jumps to the marked moment.</p>
<ul>
<li>Tap a picture for the large view and swipe to browse.</li>
<li>Date, megapixels and image size are shown at the top.</li>
<li>The bin deletes the capture from the Photos app as well. The iPhone asks first.</li>
</ul>
<p>To delete several at once, tap <kbd>Select</kbd> at the top left, tap the photos and videos you want, or <kbd>Select all</kbd>, then the bin at the bottom. The iPhone asks once for all of them.</p>
<p>The gallery needs read access to Photos. With “Limited access”, Keepsight still sees its own captures.</p>
<p>If a tile shows a cloud symbol, the original is in iCloud and is being downloaded. This happens when iCloud Photos is on with “Optimise iPhone Storage”. A warning sign means the file cannot be read; the large view then shows the file name.</p>
"""),

("flight", "Flight data", "Live flight data in the video from your own ADS-B receiver: what you need, where it works, privacy.", """
<div class="tip"><p><strong>Availability:</strong> Live flight data is available only in approved countries and regions and needs your own ADS-B receiver. At present no region is approved, so the feature stays switched off everywhere.</p></div>
<p>With the flight data overlay, Keepsight shows the flight number, altitude and speed of the airliner you are following, in the viewfinder and in the video recorded by the iPhone. The data comes from your own ADS-B receiver on the same Wi-Fi. No internet and no flight data provider are involved.</p>
<p>Keepsight follows aircraft by sight without any receiver. The receiver is needed only for the overlay, and it is not part of the app: you buy or build it separately.</p>
[[wide plane-spotting]]

<h2>What you need</h2>
<ul>
<li><strong>A receiver:</strong> a Stratux, for example a Raspberry Pi 3 with a 1090 MHz USB receiver stick and antenna, or another device that sends GDL90 over Wi-Fi.</li>
<li><strong>Not a stick alone:</strong> a USB receiver stick such as the FlightAware Pro Stick needs a host, for example a Raspberry Pi running Stratux. A standard PiAware installation sends data to FlightAware and is not suitable.</li>
<li><strong>The same Wi-Fi:</strong> the iPhone joins the receiver’s Wi-Fi. This network usually has no internet; that is fine.</li>
<li><strong>An approved region:</strong> receiving the data yourself does not by itself mean the feature is permitted in a country.</li>
</ul>

<h2>Stratux or GDL90</h2>
<table>
<tr><th>Receiver</th><th>Connection</th><th>Tested with Keepsight</th></tr>
<tr><td>Stratux (JSON)</td><td>WebSocket to the receiver, usually at 192.168.10.1</td><td>Not yet</td></tr>
<tr><td>GDL90 (UDP)</td><td>The receiver sends to port 4000 on the iPhone</td><td>Not yet</td></tr>
</table>
<p>Both are supported by protocol. No receiver has been tested with Keepsight on real hardware so far; individual devices, such as the SkyEcho 2, may behave differently. Traffic that is only sent by FLARM is not supported.</p>

<h2>Switching it on</h2>
<ol>
<li>Open the settings and switch on <kbd>Flight data overlay (ADS-B)</kbd>.</li>
<li>Read the notice and tap <kbd>Agree and enable</kbd>. Only then does iOS ask for your location.</li>
<li>Join the receiver’s Wi-Fi, choose the receiver type and enter its address. iOS asks once for access to the local network.</li>
<li>Tap <kbd>Connect receiver</kbd>. Keepsight never connects by itself.</li>
<li>Choose <kbd>Aircraft</kbd> as the subject and point the camera at the aircraft.</li>
</ol>
<p>If several aircraft fit the direction the camera is looking, Keepsight does not guess: tap <kbd>Aircraft selection required</kbd> and choose the right one.</p>
<p>You always choose the aircraft yourself, from the list of airliners currently received. The list shows the age of each position in seconds.</p>
<p>The settings show the state of the connection: connecting, connected without aircraft, receiving, or data out of date. <kbd>Reconnect</kbd> starts the connection again.</p>
<p>The flight data settings appear only while <kbd>Aircraft</kbd> is the selected subject.</p>
[[wide flight-demo]]

<h2>Why Keepsight needs your location</h2>
<p>iOS asks for your location only when you switch the flight data overlay on and agree. Keepsight needs it for two reasons:</p>
<ul>
<li><strong>Checking the region:</strong> whether flight data may be shown depends on the country you are in. Keepsight determines it from where the iPhone actually is, on the device itself.</li>
<li><strong>Recognising the aircraft in the picture:</strong> Keepsight calculates the direction and the angle above the horizon from you to each aircraft and compares them with where the camera is pointing. The compass also needs the location to find true north.</li>
</ul>
<p>Entering a place by hand is not offered, because the regional check would then no longer be reliable. If you do not use flight data, Keepsight never asks for your location.</p>

<h2>Where it works</h2>
<p>Keepsight determines the country on your iPhone from your current location. Your App Store country, language or internet address play no part. Near a border and at sea the feature stays off.</p>
<p>Every country is reviewed individually before it is approved. Until then the app tells you that live flight data is unavailable in your region. Tracking and recording work as usual.</p>

<h2>What leaves your iPhone</h2>
<p>Nothing. Keepsight only listens to the receiver and never changes its settings. Neither your location nor flight data is sent to a server.</p>
<p>Flight data exists only in the iPhone’s memory while the receiver is connected. It is deleted when you disconnect, choose another subject or leave the app. Nothing is stored or backed up.</p>

<h2>Display</h2>
<p>Flight data is shown only for scheduled passenger and cargo flights of known airlines. Private, business, military and government aircraft are never shown, and neither the registration nor the ICAO address of an aircraft appears.</p>
<p>The aircraft type is not part of ADS-B and is therefore not shown. Data that a receiver merely passes on, such as OGN, FLARM or TIS-B, is never shown either.</p>
<p>Choose the corner, compact or detailed, and metric or imperial units. Data older than 15 seconds is hidden instead of standing still. Every video with flight data carries the note “Flight data: Local ADS-B”.</p>
<p>The overlay is written into videos recorded with the iPhone. A camera on the gimbal records on its own and gets no overlay.</p>
<p>Optionally, Keepsight turns the gimbal towards the reported position of the selected aircraft while it is not yet visible in the picture. The compass limits the accuracy.</p>

<h2>Accuracy</h2>
<p>Flight data may be delayed, incomplete or wrong. It is for information only and not suitable for navigation, flight safety or operational decisions.</p>
"""),

("pro", "Free and Pro", "What the free version does, what Pro unlocks, purchase and restore.", """
<p>The free version films people in 1080p with a small Keepsight logo, without a time limit.</p>
<h2 id="simple">Simple mode</h2>
<p>New installations start in simple mode: shutter, camera switch, photo and video, and the bar at the bottom with tracking and gimbal. <kbd>Pro</kbd> at the top right opens the full view with both side panels. Without a purchase you can look at everything there; whatever carries a lock needs Keepsight Pro. <kbd>Simple mode</kbd> below the green button takes you back.</p>
<p>The handle on the left opens a small menu with <kbd>Person</kbd> and <kbd>Face</kbd>, and below them the Pro subjects with a lock; tapping one offers a preview. The gear at the bottom right opens the short settings: language, help mode, documentation, feedback and legal information. Simple mode works with DockKit gimbals only.</p>
[[shots simple simple-menu simple-photo]]
<table>
<tr><th>Feature</th><th>Free</th><th>Pro</th></tr>
<tr><td>Track person and face</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Gestures, voice commands, countdown</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Auto zoom and virtual gimbal</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Gimbal control, single shot and interval series</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Auto capture: smile, look, subject</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>All other subjects</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Drag a frame around any object</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Video resolution</td><td>1080p</td><td class="y">4K</td></tr>
<tr><td>Virtual gimbal</td><td>1080p</td><td class="y">2K</td></tr>
<tr><td>Pro tracking preview</td><td>3 × 3 minutes</td><td class="y">Unlimited</td></tr>
<tr><td>Keepsight logo in photos and videos</td><td>Yes</td><td class="y">No</td></tr>
<tr><td>FeiyuTech AK4500 and manual gimbal control</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Sound menu: microphone, headphones, spatial audio</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Overlay video</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Photos in 12 MP</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Photos up to 48 MP and in ProRAW</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Manual camera controls for photo and video</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Video in ProRes 422 HQ</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Focus follows the subject, zebra, peaking, histogram, audio meters, frame guides</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Dual capture: video with selfie picture</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Heat saver while recording, AF button</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Gimbal: framing, speaker and pan programs</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Gestures: group, framing, highlights, own assignment</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Apple Watch: shutter, mode, tracking, status</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Apple Watch: alerts, controls, live view, highlights</td><td>No</td><td class="y">Yes</td></tr>
</table>

<h2>Trying Pro tracking</h2>
<p>Tap a locked subject in the tracking panel and choose <kbd>Start preview</kbd>. For 3 minutes Keepsight follows this subject exactly as the Pro version does. The time only runs while a subject is being followed, so waiting costs nothing. You have three such sessions; one that fails within the first seconds does not count. To test the FeiyuTech AK4500, touch and hold the gimbal symbol in the full view, choose FeiyuTech AK4500 and start a preview there.</p>
<p>If the iPhone’s storage is almost full, Keepsight does not start a recording, and it stops and saves a running recording in time.</p>

<h2>Buying Pro</h2>
<p>Tap <kbd>PRO</kbd> at the top right and then <kbd>Unlock</kbd>. Pro is a one-time purchase without a subscription. The App Store shows the price in your currency and Apple handles the payment.</p>

<h2>Restoring a purchase</h2>
<p>On a new iPhone or after reinstalling, tap <kbd>PRO</kbd> → <kbd>Restore purchase</kbd>. You must be signed in with the same Apple Account you used for the purchase.</p>
<p>Have a code for Keepsight Pro? Tap <kbd>PRO</kbd> → <kbd>Redeem code</kbd> and enter it. Apple checks the code; it unlocks Pro just like a purchase.</p>

<h2>Refunds</h2>
<p>Request a refund from Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
"""),

("settings", "Settings and help", "Language, help mode and the controls for advanced users.", """
[[shots settings settings-models]]
[[shots settings-gestures settings-monitoring]]
<p>The most important switches are in the two side panels. Everything else is in the left panel under <kbd>All settings</kbd>.</p>
<h2>Help mode</h2>
<p>The question mark at the top of each side panel switches help mode on. Yellow hints with a short explanation then appear under the menu items, with a diagram for the important ones.</p>

<h2>Language</h2>
<p>Keepsight uses the language of your iPhone. To choose a different one for Keepsight only, tap <kbd>Language</kbd> under <kbd>All settings</kbd>. This opens the iPhone settings for Keepsight. The voice commands change with it.</p>

<h2>Controls for advanced users</h2>
<table>
<tr><th>Setting</th><th>Meaning</th></tr>
<tr><td>Speed “Custom”</td><td>Gain, damping, top speed, acceleration and calm zone of the tracking.</td></tr>
<tr><td>Minimum speed</td><td>For the AK4500 only: the smallest command the gimbal still reacts to. Raise it if the gimbal stops at small deviations.</td></tr>
<tr><td>Prediction after loss</td><td>How long the gimbal keeps panning when the subject is hidden.</td></tr>
<tr><td>Direction</td><td>Invert pan or tilt.</td></tr>
<tr><td>Detection model</td><td>Which model detects a subject. RF-DETR Small and YOLOX-S are available.</td></tr>
<tr><td>Reset to defaults</td><td>Restores the tracking controls.</td></tr>
</table>

<h2>About and licenses</h2>
<p>Here you find the app version, links to this website and the licenses of the detection models used.</p>
"""),

("troubleshooting", "Troubleshooting", "Common problems and how to solve them.", """
<h2>The gimbal is not found</h2>
<ul>
<li><strong>Device with DockKit:</strong> Is it paired in the iPhone settings and is the iPhone seated properly in the mount? For comparison, open Apple’s Camera app. If the device does not follow you there, the pairing is the problem.</li>
<li><strong>AK4500:</strong> Is the gimbal switched on and nearby? Close the Feiyu app completely and allow Bluetooth under <kbd>Settings</kbd> → <kbd>Keepsight</kbd>.</li>
<li>Switch the gimbal off and on again and connect once more.</li>
</ul>
<h2>The gimbal turns away from the subject</h2>
<p>Keepsight normally corrects this by itself after a moment. If not, invert the affected axis under <kbd>All settings</kbd> → <kbd>Direction</kbd>.</p>
<h2>The gimbal reacts sluggishly or shakes</h2>
<ul>
<li>Sluggish: choose the Sport profile. With the AK4500 a higher minimum speed also helps.</li>
<li>Shaking or swinging: choose the Smooth profile. With a long focal length small movements appear larger.</li>
</ul>
<h2>The subject is not detected</h2>
<ul>
<li>Is the right subject type selected?</li>
<li>Very small subjects are detected less reliably. Choose a longer lens.</li>
<li>Detection drops in low light and strong backlight.</li>
</ul>
<h2>Voice commands are not understood</h2>
<ul>
<li>Allow the microphone and speech recognition under <kbd>Settings</kbd> → <kbd>Keepsight</kbd>.</li>
<li>Speak the commands in the app’s language.</li>
<li>For photo and video, say at least two words, for example “take a photo” or “start video”.</li>
<li>Wind and loud surroundings disturb recognition. Gestures are more reliable then.</li>
</ul>
<h2>Gestures do not trigger</h2>
<ul>
<li>The subject must be set to Person or Face.</li>
<li>Keep your hand still and clearly visible until the bar is full.</li>
<li>Only the tracked person can give gestures, or without tracking the largest person in the picture.</li>
<li>After a gesture, wait 2 seconds before the next one.</li>
<li>For ☝️ keep the thumb against your hand; for the L spread it out. That is how Keepsight tells the two apart.</li>
</ul>
<h2>48 MP or RAW cannot be selected</h2>
<p>Both are only available in photo mode and with a lens that supports them. On the iPhone 15 Pro that is only the main camera <kbd>1×</kbd>; newer Pro models also offer 48 MP with other lenses. 48 MP and RAW also require Keepsight Pro.</p>
<h2>The gallery is empty</h2>
<p>Allow Keepsight access to Photos. Captures from older versions of the app do not appear in the gallery, but they are in the Photos app.</p>
<h2>Keepsight Pro is not active after purchase</h2>
<p>Tap <kbd>PRO</kbd> → <kbd>Restore purchase</kbd> and check that you are signed in with the right Apple Account.</p>
<h2>More help</h2>
<p>Write to <a href="mailto:keepsight.support@gmail.com">keepsight.support@gmail.com</a> and include your iPhone model, iOS version and the Keepsight version.</p>
<h2>The iPhone gets hot</h2>
<p>Detection, 4K recording and gimbal control are demanding, especially in the sun. Keepsight protects the device by itself:</p>
<ul>
<li><strong>Thermometer in the status field:</strong> the iPhone is hot and detection only evaluates every second or third frame. Tracking continues but reacts a little more slowly.</li>
<li><strong>Tracking stopped:</strong> at a critical temperature Keepsight ends tracking and recording and saves the video. Let the iPhone cool down in the shade.</li>
</ul>
<p>To keep it cooler: switch off detection and gesture control when you do not need them, 1080p instead of 4K, 30 instead of 60 frames, switch off the overlay video and virtual gimbal, remove the case. For this reason the iPhone 12 and older models start with 1080p.</p>
"""),
]

SUPPORT = {
    "title": "Support",
    "lead": "The documentation answers most questions. If you get stuck, write to me.",
    "body": f"""
<h2>Contact</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>
<p>In the app, <kbd>Send feedback</kbd> in the settings prepares this email with the technical details for you.</p>
<p>So I can help quickly, please include:</p>
<ul>
<li>your iPhone model and iOS version</li>
<li>the Keepsight version (in the app under All settings → About and licenses)</li>
<li>what you did and what happened instead, ideally with a screenshot or short video</li>
</ul>
<h2>Quick help</h2>
<ul>
<li><a href="docs/start.html">Getting started</a>: permissions and connecting the gimbal</li>
<li><a href="docs/troubleshooting.html">Troubleshooting</a>: common problems and how to solve them</li>
<li><a href="docs/pro.html">Free and Pro</a>: purchase, restore, refunds</li>
</ul>
""",
}

PRIVACY = {
    "title": "Privacy Policy",
    "lead": "Last updated: 18 November 2026. Applies to the Keepsight iOS app and this website.",
    "body": f"""
<div class="tip"><p><strong>In short:</strong> Keepsight does not collect data about you. There is no account, no advertising, no tracking and no analytics. Camera images, detection, photos and videos stay on your iPhone.</p></div>
<h2>1. Controller</h2>
<p>{ADDRESS}<br>Email: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>2. What the app processes</h2>
<p>The app processes data only on your device and only to provide its features. I, as the provider, receive none of it.</p>
<ul>
<li><strong>Camera:</strong> The camera image is analysed on the iPhone to detect and follow subjects. Images do not leave the device.</li>
<li><strong>Faces:</strong> to detect faces, smiles and where people look, the app analyses the camera image on the iPhone. It does not recognise who someone is and stores no facial features. Portrait photos contain depth data from the front camera; it exists only in the photo you save yourself.</li>
<li><strong>Microphone:</strong> for the sound of your videos and, if you turn on voice control, for voice commands.</li>
<li><strong>Speech recognition:</strong> Voice commands are recognised by Apple’s speech recognition. If your iPhone and the selected language support it, this happens on the device. Otherwise the audio is sent to Apple for recognition, subject to Apple’s privacy policy. Voice control is off by default.</li>
<li><strong>Photos:</strong> The app saves your captures to the photo library and shows only captures made with Keepsight in its gallery. If you use iCloud Photos, Apple transfers them according to your iCloud settings.</li>
<li><strong>Bluetooth:</strong> to control your gimbal. Only control commands and status values are exchanged with the gimbal.</li>
<li><strong>Apple Watch:</strong> The watch app talks only to your own iPhone through Apple’s WatchConnectivity. Status, commands and the small live image go directly between your two devices. The watch stores nothing.</li>
<li><strong>Location and flight data:</strong> only if you switch on the flight data overlay and agree to it. Keepsight then uses your location on the iPhone to determine the region and to recognise the aircraft in the picture. The flight data comes from your own ADS-B receiver on the local network. Neither your location nor flight data leaves the iPhone. Without this feature the app does not use your location.</li>
<li><strong>Local network:</strong> only for the flight data overlay, to reach your own ADS-B receiver. Keepsight only receives data from it.</li>
<li><strong>Settings:</strong> Your in-app settings are stored locally on the iPhone only.</li>
</ul>
<h2>3. Purchases</h2>
<p>The purchase of “Keepsight Pro” is handled by Apple through the App Store. I receive no payment details, name or email address, only aggregated sales figures from Apple.</p>
<h2>4. Test versions (TestFlight)</h2>
<p>If you use a test version through TestFlight, Apple processes your email address for the invitation and, if you agree, crash reports and your feedback. I see feedback and crash reports in order to fix problems, and the email addresses of testers I invited myself.</p>
<h2>5. Contact by email</h2>
<p>If you write to me, I use your email address and the content of your message only to reply. I delete messages once the matter is resolved, after two years at the latest.</p>
<p>The feedback function in the app only prepares an email with technical details such as app version, iPhone model, iOS version and gimbal type. You see the whole text and send it yourself.</p>
<h2>6. This website</h2>
<p>This website sets no cookies and uses no tracking. Fonts and scripts are served from the same site; no third-party content is loaded. Your language choice is stored only in your browser. The site is hosted on GitHub Pages (GitHub, Inc., USA). When you visit, GitHub processes technically necessary data such as your IP address in server logs. See GitHub’s privacy statement for details.</p>
<h2>7. Your rights</h2>
<p>Under the Swiss Data Protection Act and, where applicable, the GDPR, you have the right to access, rectification, erasure, restriction of processing and data portability, and the right to lodge a complaint with a supervisory authority (in Switzerland the FDPIC). Because the app sends no data to me, in practice this concerns only emails you have sent me. Write to <a href="mailto:{MAIL}">{MAIL}</a>.</p>
<h2>8. Children</h2>
<p>The app is not directed at children and does not collect data from them.</p>
<h2>9. Changes</h2>
<p>If the app changes in a way that requires changes to this policy, it will be updated here. The version on this page applies.</p>
""",
}

IMPRINT = {
    "title": "Imprint",
    "lead": "",
    "body": f"""
<h2>Provider</h2>
<p>{ADDRESS}</p>
<p>Email: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>Liability</h2>
<p>Keepsight controls a motorised gimbal. Make sure the gimbal can move freely and nobody is put at risk. Use is at your own responsibility, to the extent permitted by law.</p>
<h2>Trademarks</h2>
<p>Apple, iPhone, App Store, TestFlight and DockKit are trademarks of Apple Inc. FeiyuTech, AK4500, Insta360, DJI and Belkin are trademarks of their respective owners. Keepsight is an independent product and is not affiliated with these companies.</p>
<h2>Terms of use</h2>
<p>The app is licensed under Apple’s standard licence agreement for apps: <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Licensed Application End User License Agreement</a>.</p>
<h2>Typeface</h2>
<p>This website uses the Inter typeface (SIL Open Font License 1.1).</p>
""",
}

# Bildunterschriften der Bildschirmfotos
SHOTS = {'simple': 'Simple mode', 'simple-menu': 'Tracking', 'simple-photo': 'Photo', 'pro-exposure': 'Manual controls: exposure, ISO and shutter, shown with help mode', 'pro-aperture': 'Manual controls: white balance, tint, focus and aperture', 'camera': 'Camera panel: format, manual controls and monitoring', 'camera-zoom': 'Camera panel: monitoring, auto zoom and virtual gimbal', 'format-video': 'Format in video mode', 'format-photo': 'Format in photo mode', 'settings': 'Settings: speed, gimbal, quality', 'settings-models': 'Settings: detection model and direction', 'settings-gestures': 'Settings: gestures, recording and dual capture', 'settings-monitoring': 'Settings: recording, dual capture and monitoring', 'tracking-help': 'Tracking panel with subject, speed and remote control, shown with help mode', 'tracking': 'Tracking panel: detection, subject, speed and remote control', 'manual': 'Manual section with joystick', 'flight-demo': 'Example of the overlay (illustration). With a local receiver the aircraft type is not shown.', 'hero': 'A young woman films herself and her friends with a phone on a gimbal at sunset', 'story-family': 'A family on a picnic blanket by a lake, filmed by a phone on a small gimbal', 'story-sport': 'A woman films a passing cyclist with a phone on a gimbal', 'story-pets': 'A man films a running dog and a child with a phone on a gimbal', 'story-birds': 'A photographer follows a bird of prey in flight with a camera on a gimbal', 'story-pro': 'A woman with a camera on a gimbal and a phone in her hand while an aircraft passes overhead', 'story-aviation': 'Plane spotters at an airport fence film an airliner with a phone on a gimbal', 'plane-spotting': 'Plane spotting with a phone on a gimbal (illustration)', 'sound': 'Sound menu: choose the microphone and switch the level meter'}
