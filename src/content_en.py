"""English content of the Keepsight website."""

MAIL = "ar.orca@gmail.com"
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
    "finder_status": "Target locked",
    "finder_caption": "Virtual gimbal frame",
}

HOME = {
    "title": "Keepsight: your subject stays in frame",
    "description": "Keepsight detects people, aircraft, birds and more, and steers your gimbal to follow them. Detection runs on the iPhone.",
    "h1": "Your subject stays in frame.",
    "lead": "Keepsight recognises what you are filming and steers your gimbal to follow it. All detection runs on your iPhone.",
    "cta": "Read the documentation",
    "note": "Keepsight is currently in beta testing and not yet available on the App Store.",
    "rig_h": "Built for the big camera",
    "rig_p": [
        "Keepsight was made for one particular rig: a strong gimbal carries a mirrorless camera, for example a Lumix S1RII filming in 8K. The iPhone sits on top. It detects the subject and steers the gimbal, while the camera underneath takes the actual footage.",
        "You get a tracked shot in the quality of your best camera, through your own lenses, without panning by hand and without a second person on the gimbal.",
        "Photos and videos from the iPhone itself are a bonus: a second angle, a reference picture, or for the days the big camera stays at home.",
    ],
    "rig_link": "Set up the rig step by step",
    "rig_labels": ("iPhone: detects and steers", "Camera: records", "Gimbal: follows"),
    "rig_alt": "Gimbal carrying a mirrorless camera with the iPhone on top; both look at the same aircraft",
    "shots_h": "What the app looks like",
    "what_h": "What Keepsight does for you",
    "what": [
        ("Follow", "Choose a subject: person, face, aircraft, bird, animal, vehicle, train or boat. Keepsight keeps it centred and steers the gimbal. If a cloud hides the aircraft, the app briefly keeps following its path."),
        ("Zoom", "Auto zoom keeps the subject at the size you set. It moves in tiny steps and stays within the selected lens, so the video never jumps."),
        ("Frame", "The virtual gimbal saves a second video whose frame follows the subject smoothly and zooms by itself. It works handheld too, without a gimbal."),
        ("Shoot", "With Keepsight Pro the app takes the photo by itself when everyone smiles, when everyone looks at the camera, or when the subject is large enough in the frame. Interval series, hand gestures and voice commands with a countdown are already part of the free version."),
    ],
    "cam_h": "The full camera of your iPhone",
    "cam": [("4K", "Video at 24, 25, 30 or 60 frames per second"),
            ("48 MP", "Photos with the main camera, as HEIF or ProRAW"),
            ("3", "Lenses: ultra wide, main camera and telephoto")],
    "price_h": "Try it free, buy it once",
    "price_p": "The free version lets you test everything on people. Keepsight Pro is unlocked with a single purchase, no subscription. The App Store shows the price in your currency.",
    "price_rows": [
        ("Track person and face", True, True),
        ("Gestures, voice commands, countdown", True, True),
        ("Auto zoom and virtual gimbal", True, True),
        ("Gimbal control with Apple DockKit", True, True),
        ("4K video and 48 MP photos", True, True),
        ("Auto capture: smile, look, subject", False, True),
        ("Aircraft, bird, animal, vehicle, train, boat", False, True),
        ("Drag a frame around any object", False, True),
        ("Video up to 60 seconds, with logo", True, True),
        ("Pro tracking preview: 3 × 60 seconds", True, True),
        ("Recording without time limit or logo", False, True),
        ("Second video with frames and data", False, True),
        ("Photos in ProRAW", False, True),
    ],
    "price_cols": ("Feature", "Free", "Pro"),
    "price_note": "In the free version, videos are limited to 60 seconds and carry the Keepsight logo.",
    "free_line": "Up to 60 seconds of free filming.",
    "try_h": "Try Keepsight for free",
    "try": [
        "Videos of up to 60 seconds with the Keepsight logo, as often as you like.",
        "Pro tracking preview: 3 sessions of 60 seconds each, with a Pro subject of your choice.",
        "Test your subject and your gimbal before you buy.",
    ],
    "pro_card": "Buy once. Unlock for good. No recurring subscription costs.",
    "campaign": {
        "prelaunch": "Planned for the launch in the Swiss App Store: CHF 14.90 as a one-time purchase until 31 March 2027 inclusive, CHF 19.90 from 1 April 2027.",
        "intro": ("Launch price: CHF 14.90 – one-time, no subscription.", "Only until 31 March 2027 inclusive.", "From 1 April 2027: CHF 19.90."),
        "regular": "Keepsight Pro – CHF 19.90 one-time. No subscription.",
        "unverified": "The App Store shows the current price in your currency.",
        "swiss": "Prices in Swiss francs apply to the Swiss App Store. In other countries the App Store shows the price in your currency.",
        "store": "Download on the App Store",
    },
    "faq_h": "Questions and answers",
    "faq": [
        ("Do I pay once or regularly?", "Once. Keepsight Pro is a one-time purchase, with no subscription and no recurring costs."),
        ("What can I do for free?", "Follow people and faces, use gestures, voice commands, auto zoom and the virtual gimbal, and film videos of up to 60 seconds with the Keepsight logo. You can also try Pro tracking three times for 60 seconds."),
        ("How do I restore my purchase?", "In the app, open the Pro screen and choose to restore the purchase. You must be signed in with the Apple Account you bought with."),
        ("Why does the price differ in my country?", "Apple sets the price per country and currency, including taxes. The price shown in your App Store is the one that applies."),
        ("Does Keepsight work without internet?", "Yes. Detection and tracking run on the iPhone. Internet is needed only for the purchase and for the optional flight data."),
        ("What happens to my pictures?", "They stay on your iPhone. Keepsight has no account, no advertising and no analytics."),
        ("Does Keepsight record with my big camera?", "No. Keepsight steers the gimbal; the camera on it records on its own. Keepsight's own photos and videos come from the iPhone camera."),
        ("Is live flight data available where I live?", "Only in supported countries and regions, and it needs location access and internet. At present no region is approved."),
    ],
    "need_h": "What you need",
    "need": [
        ("iPhone", "An iPhone with iOS 17 or later. Keepsight is developed and tested on the iPhone 15 Pro Max with three cameras."),
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
</table>
<p>If you declined an access, you can allow it later under <kbd>Settings</kbd> → <kbd>Keepsight</kbd>.</p>

<h2>Connecting the gimbal</h2>
<ul>
<li><strong>Gimbal or stand with Apple DockKit:</strong> Pair the device with your iPhone once, as the manufacturer describes. After that, Keepsight connects by itself when you mount the iPhone.</li>
<li><strong>FeiyuTech AK4500:</strong> Switch the gimbal on and tap <kbd>Connect</kbd> at the bottom right in Keepsight.</li>
</ul>
<p>Once connected, the button changes to <kbd>Track</kbd>. Details are in the chapter <a href="gimbals.html">Supported gimbals</a>.</p>
<div class="tip"><p>The gimbal must be able to turn freely. Keep fingers, cables and objects out of its range of movement.</p></div>

<h2>Your first tracking</h2>
<ol>
<li>Open the left panel and choose the subject <kbd>Person</kbd>.</li>
<li>Step in front of the camera. A frame appears around you and the status at the top left reads “Target locked”.</li>
<li>Tap <kbd>Track</kbd>. The gimbal follows you.</li>
<li><kbd>Stop</kbd> ends the tracking.</li>
</ol>
<p>If the gimbal turns away from the subject instead of towards it, invert the axis under <kbd>All settings</kbd> → <kbd>Direction</kbd>.</p>
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
<li>Mount the iPhone and open Keepsight. The app detects the device by itself and the button at the bottom right shows <kbd>Track</kbd>.</li>
<li>Choose a subject and tap <kbd>Track</kbd>.</li>
</ol>
<p>While Keepsight controls the device, Apple’s own tracking is switched off so the two do not interfere. If you disconnect in the <kbd>Manual</kbd> area, the system takes over again.</p>
<p>DockKit requires iOS 17 or later. Keepsight cannot control devices without DockKit, such as older models from the same manufacturers.</p>

<h2>FeiyuTech AK4500</h2>
<ol>
<li>Switch the gimbal on. Close the Feiyu app, because the gimbal accepts only one connection.</li>
<li>Tap <kbd>Connect</kbd> at the bottom right in Keepsight.</li>
<li>Allow Bluetooth access the first time.</li>
</ol>
<p>The AK4500 only reacts above a certain command strength. Keepsight compensates for this with the <kbd>Minimum speed</kbd> setting, see the Settings chapter.</p>

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
<li>Choose the subject in Keepsight and tap <kbd>Track</kbd>.</li>
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
<tr><td>Button on the right</td><td>Connect, Track or Stop.</td></tr>
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
<p>Keepsight rotates its interface when you turn the iPhone to landscape. During a video recording the image format stays fixed.</p>
"""),

("tracking", "Tracking subjects", "Subject types, custom target, speed and behaviour when the subject is hidden.", """
[[shots tracking-help]]
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
</table>
<h3>Photo</h3>
<table>
<tr><th>Setting</th><th>Options</th></tr>
<tr><td>Format</td><td>HEIF or RAW (Apple ProRAW, with Keepsight Pro)</td></tr>
<tr><td>Resolution</td><td>Whatever the lens delivers, see below</td></tr>
</table>

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
<tr><td><kbd>.5×</kbd> ultra wide</td><td>12 MP</td></tr>
<tr><td><kbd>1×</kbd> main camera</td><td>12, 24 or 48 MP; in RAW 12 or 48 MP</td></tr>
<tr><td><kbd>5×</kbd> telephoto</td><td>12 MP</td></tr>
</table>
<p>These values apply to the iPhone 15 Pro Max. The format panel only ever shows what the current lens really delivers.</p>
<div class="tip"><p>A photo triggered by gesture or voice in video mode has about 10 MP. Switch to photo mode for the full resolution.</p></div>
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

("virtual-gimbal", "Virtual gimbal", "A second video with a smoothly following, zooming frame.", """
<p>The virtual gimbal cuts a frame out of the full camera image that follows the subject and zooms by itself. The result is a finished, calm video, available right after recording.</p>
<h2>Turning it on</h2>
<ol>
<li>Open the right panel and switch on <kbd>Virtual gimbal</kbd>.</li>
<li>Choose a subject. In the viewfinder you see the frame as a bright outline; the area outside is dimmed.</li>
<li>Start recording.</li>
</ol>
<p>A real gimbal is not needed. You can hold the iPhone in your hand or put it on a tripod. Together with a gimbal and auto zoom the image becomes calmer still.</p>

<h2>Settings</h2>
<table>
<tr><th>Control</th><th>Effect</th></tr>
<tr><td>Free space around subject</td><td>10 to 40 percent. More space looks calmer, less space brings the subject closer.</td></tr>
<tr><td>Maximum zoom</td><td>1.5× to 4×. When recording in 4K, full sharpness is kept up to 2×.</td></tr>
<tr><td>Smoothness</td><td>How leisurely the frame follows. Larger values smooth more.</td></tr>
<tr><td>Also save original</td><td>Saves the full video alongside the framed one.</td></tr>
</table>

<h2>What is saved</h2>
<ul>
<li>The framed video in 1080p.</li>
<li>Optionally the original in the selected resolution.</li>
</ul>
<p>If Keepsight loses the subject, the frame slowly returns to the full image.</p>
<div class="tip"><p>The virtual gimbal keeps the subject steady in the frame. It does not compensate for strong shake of the background.</p></div>
"""),

("photo", "Photos and triggers", "Single shot, interval series and automatic capture at the right moment.", """
[[shots camera]]
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
[[shots settings-gestures]]
<p>You find all three in the left panel under <kbd>Remote control</kbd>.</p>
<h2>Hand gestures</h2>
<p>Gestures work when the subject is set to Person or Face. Hold the gesture still for about half a second. A bar fills at the top centre while you do.</p>
<table>
<tr><th>Gesture</th><th>Effect</th></tr>
<tr><td>Open hand</td><td>Start or stop video recording.</td></tr>
<tr><td>OK sign</td><td>Choose this person as the target and start tracking.</td></tr>
<tr><td>Peace sign</td><td>Take a photo.</td></tr>
<tr><td>Two open hands</td><td>Stop tracking.</td></tr>
</table>

<h2>Voice commands</h2>
<p>Switch on <kbd>Voice control</kbd> and allow the microphone and speech recognition. Speak the commands in the app’s language.</p>
<table>
<tr><th>You say</th><th>Effect</th></tr>
<tr><td>“Photo”</td><td>Take a photo.</td></tr>
<tr><td>“Start video” or “Start recording”</td><td>Start video recording.</td></tr>
<tr><td>“Stop”</td><td>End the recording, the series or a running countdown.</td></tr>
</table>
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

("recording", "Recording and gallery", "Which videos are created, where they are and how to view them.", """
<h2>Recording video</h2>
<p>In video mode the red shutter starts and stops the recording. The time runs at the top centre. Videos have sound and are saved to the Photos app.</p>

<h2>Which videos are created</h2>
<table>
<tr><th>Video</th><th>Content</th><th>When</th></tr>
<tr><td>Original</td><td>The clean camera image in the selected resolution.</td><td>Always, unless you switch it off for the virtual gimbal.</td></tr>
<tr><td>Virtual gimbal</td><td>The following frame in 1080p.</td><td>When the virtual gimbal is on.</td></tr>
<tr><td>Overlay video</td><td>The image with frames, time, subject, status and gimbal data in 1080p.</td><td>With Keepsight Pro, when <kbd>Overlay video</kbd> is on.</td></tr>
</table>

<h2>Gallery</h2>
<p>The thumbnail above the mode switch shows the latest capture. Tap it to open the gallery with all photos and videos you made with Keepsight, newest first.</p>
<ul>
<li>Tap a picture for the large view and swipe to browse.</li>
<li>Date, megapixels and image size are shown at the top.</li>
<li>The bin deletes the capture from the Photos app as well. The iPhone asks first.</li>
</ul>
<p>The gallery needs read access to Photos. With “Limited access”, Keepsight still sees its own captures.</p>
<p>If a tile shows a cloud symbol, the original is in iCloud and is being downloaded. This happens when iCloud Photos is on with “Optimise iPhone Storage”. A warning sign means the file cannot be read; the large view then shows the file name.</p>
"""),

("flight", "Flight data", "Live flight data in the video: where it is available, consent, sources.", """
<div class="tip"><p><strong>Availability:</strong> Live flight data is available only in supported countries and regions; location access and internet are required. At present no region is approved, so the feature stays switched off everywhere.</p></div>
<p>With the flight data overlay, Keepsight shows the callsign, aircraft type, altitude and speed of the aircraft you are following, in the viewfinder and in the recorded video. The data comes from adsb.lol, a community network of ADS-B receivers.</p>

<h2>Switching it on</h2>
<ol>
<li>Open the settings and switch on <kbd>Flight data overlay (ADS-B)</kbd>.</li>
<li>Read the notice and tap <kbd>Agree and enable</kbd>. Only then does iOS ask for your location.</li>
<li>Choose <kbd>Aircraft</kbd> as the subject and point the camera at the aircraft.</li>
</ol>
<p>If several aircraft fit the direction the camera is looking, Keepsight does not guess: tap <kbd>Aircraft selection required</kbd> and choose the right one.</p>

<h2>Why Keepsight needs your location</h2>
<p>iOS asks for your location only when you switch the flight data overlay on and agree. Keepsight needs it for three reasons:</p>
<ul>
<li><strong>Checking the region:</strong> whether flight data may be shown depends on the country you are in. Keepsight determines it from where the iPhone actually is, on the device itself.</li>
<li><strong>Finding aircraft nearby:</strong> the data provider answers the question “which aircraft are around this point?”. Without your position there is no point to ask about.</li>
<li><strong>Recognising the aircraft in the picture:</strong> Keepsight calculates the direction and the angle above the horizon from you to each aircraft and compares them with where the camera is pointing. The compass also needs the location to find true north.</li>
</ul>
<p>Entering a place by hand is not offered, because the regional check would then no longer be reliable. If you do not use flight data, Keepsight never asks for your location.</p>

<h2>Where it works</h2>
<p>Keepsight determines the country on your iPhone from your current location. Your App Store country, language or internet address play no part. Near a border and at sea the feature stays off.</p>
<p>Every country is reviewed individually before it is approved. Until then the app tells you that live flight data is unavailable in your region. Tracking and recording work as usual.</p>

<h2>What is sent</h2>
<p>Only while the feature is active does Keepsight send your location, rounded to about one kilometre, to adsb.lol to find nearby aircraft. Nothing is sent before you agree, and nothing in regions that are not approved.</p>

<h2>Display</h2>
<p>Choose the corner, compact or detailed, and metric or imperial units. Data older than 15 seconds is hidden. Every video with flight data carries the credit “Data: adsb.lol · ODbL 1.0”.</p>
<p>The overlay is written into videos recorded with the iPhone. A camera on the gimbal records on its own and gets no overlay.</p>

<h2>Accuracy</h2>
<p>Flight data may be delayed, incomplete or wrong. It is for information only and not suitable for navigation, flight safety or operational decisions.</p>
"""),

("pro", "Free and Pro", "What the free version does, what Pro unlocks, purchase and restore.", """
<p>The free version is for trying things out: you test following, gestures and the camera on people before paying anything.</p>
<table>
<tr><th>Feature</th><th>Free</th><th>Pro</th></tr>
<tr><td>Track person and face</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Gestures, voice commands, countdown</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Auto zoom and virtual gimbal</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Gimbal control, single shot and interval series</td><td class="y">Yes</td><td class="y">Yes</td></tr>
<tr><td>Auto capture: smile, look, subject</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>All other subjects</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Drag a frame around any object</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Video length</td><td>60 seconds</td><td class="y">Unlimited</td></tr>
<tr><td>Pro tracking preview</td><td>3 × 60 seconds</td><td class="y">Unlimited</td></tr>
<tr><td>Keepsight logo in photos and videos</td><td>Yes</td><td class="y">No</td></tr>
<tr><td>Overlay video</td><td>No</td><td class="y">Yes</td></tr>
<tr><td>Photos in ProRAW</td><td>No</td><td class="y">Yes</td></tr>
</table>

<h2>Trying Pro tracking</h2>
<p>Tap a locked subject in the tracking panel and choose <kbd>Start preview</kbd>. For 60 seconds Keepsight follows this subject exactly as the Pro version does. You have three such sessions; one that fails within the first seconds does not count.</p>
<p>In the free version a video ends by itself after 60 seconds. A note appears 10 seconds before the end.</p>

<h2>Buying Pro</h2>
<p>Tap <kbd>PRO</kbd> at the top right and then <kbd>Unlock</kbd>. Pro is a one-time purchase without a subscription. The App Store shows the price in your currency and Apple handles the payment.</p>

<h2>Restoring a purchase</h2>
<p>On a new iPhone or after reinstalling, tap <kbd>PRO</kbd> → <kbd>Restore purchase</kbd>. You must be signed in with the same Apple Account you used for the purchase.</p>

<h2>Refunds</h2>
<p>Request a refund from Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
"""),

("settings", "Settings and help", "Language, help mode and the controls for advanced users.", """
[[shots settings settings-models settings-gestures]]
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
<tr><td>Developer info</td><td>Shows frame rate, gimbal commands and model timing in the viewfinder.</td></tr>
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
<li>Switch the gimbal off and on again and tap <kbd>Connect</kbd> once more.</li>
</ul>
<h2>The gimbal turns away from the subject</h2>
<p>Invert the affected axis under <kbd>All settings</kbd> → <kbd>Direction</kbd>.</p>
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
<li>Wind and loud surroundings disturb recognition. Gestures are more reliable then.</li>
</ul>
<h2>Gestures do not trigger</h2>
<ul>
<li>The subject must be set to Person or Face.</li>
<li>Keep your hand still and clearly visible until the bar is full.</li>
</ul>
<h2>48 MP or RAW cannot be selected</h2>
<p>Both are only available in photo mode with the main camera <kbd>1×</kbd>. RAW also requires Keepsight Pro.</p>
<h2>The gallery is empty</h2>
<p>Allow Keepsight access to Photos. Captures from older versions of the app do not appear in the gallery, but they are in the Photos app.</p>
<h2>Keepsight Pro is not active after purchase</h2>
<p>Tap <kbd>PRO</kbd> → <kbd>Restore purchase</kbd> and check that you are signed in with the right Apple Account.</p>
<h2>More help</h2>
<p>Write to <a href="mailto:ar.orca@gmail.com">ar.orca@gmail.com</a> and include your iPhone model, iOS version and the Keepsight version.</p>
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
    "lead": "Last updated: 14 November 2026. Applies to the Keepsight iOS app and this website.",
    "body": f"""
<div class="tip"><p><strong>In short:</strong> Keepsight does not collect data about you. There is no account, no advertising, no tracking and no analytics. Camera images, detection, photos and videos stay on your iPhone. The one exception is the optional flight data feature, which sends an approximate location to a data provider (see section 2).</p></div>
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
<li><strong>Location and flight data:</strong> only if you switch on the flight data overlay and agree to it. Keepsight then uses your location on the iPhone to determine the region and, where the feature is approved, sends the location rounded to about one kilometre to the provider adsb.lol to find nearby aircraft. I cannot say whether or how long adsb.lol keeps such requests; its own terms apply. The transmission stops when you switch the feature off. Without this feature the app does not use your location.</li>
<li><strong>Settings:</strong> Your in-app settings are stored locally on the iPhone only.</li>
</ul>
<h2>3. Purchases</h2>
<p>The purchase of “Keepsight Pro” is handled by Apple through the App Store. I receive no payment details, name or email address, only aggregated sales figures from Apple.</p>
<h2>4. Test versions (TestFlight)</h2>
<p>If you use a test version through TestFlight, Apple processes your email address for the invitation and, if you agree, crash reports and your feedback. I see feedback and crash reports in order to fix problems, and the email addresses of testers I invited myself.</p>
<h2>5. Contact by email</h2>
<p>If you write to me, I use your email address and the content of your message only to reply. I delete messages once the matter is resolved, after two years at the latest.</p>
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
SHOTS = {'camera': 'Camera panel: format, zoom, virtual gimbal, photo trigger', 'format-video': 'Format in video mode', 'format-photo': 'Format in photo mode', 'settings': 'Settings: speed, gimbal, quality', 'settings-models': 'Settings: detection model and direction', 'settings-gestures': 'Settings: gestures, recording, language', 'tracking-help': 'Tracking panel with subject, speed and remote control, shown with help mode', 'manual': 'Manual section with joystick'}
