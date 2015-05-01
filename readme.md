<h1>UKStationLive</h1>
![ukstationlive](https://s3-eu-west-1.amazonaws.com/ukstationliveimg/ukstationlivepub.png)

UKStationLive is a live endpoint client powered by [Huxley](https://github.com/jpsingleton/Huxley/) and National Rail's live Darwin Service. The client is open sourced under the GPL 3.0 free software license.

Using the Cloud (S3) to pull station CRS codes, grab data from the JSON station Huxley service (Azure) and provide a multiplatform experience. Simply put this app allows you to view when trains will be arriving at a platform, What platform they are arriving from, The origin of the train and the final destination of the train.

We have support for all 2564 stations across the United Kingdom.


<h2>Requirements</h2>
[Requests](http://docs.python-requests.org/en/latest/) Module (pip install requests)

[Huxley](https://github.com/jpsingleton/Huxley/wiki/Hosting-Quick-Start)

[Python 3](http://python.org)

[National Rail API key](http://realtime.nationalrail.co.uk/OpenLDBWSRegistration) - Please use your own API key.
Access to the internet.

<h2>Setup</h2>
edit the config.json file in your own text editor, We personally <3 [Atom](http://atom.io)

Be sure to replace the following items.

1) The Huxley Proxy url with [your own Huxley proxy](https://github.com/jpsingleton/Huxley/wiki/Hosting-Quick-Start).
2) The API key. [Click here to sign up for the National Rail API](http://realtime.nationalrail.co.uk/OpenLDBWSRegistration)

<h2>Station CSRs</h2>
On the first weekend of each month, we will update the station CSRs. These will be pushed out to the client over the air. a copy will also be included with the github repo allowing you to host your own copy of the CSR codes.

**Host your own copy of stations.json**

[![Download](https://s3-eu-west-1.amazonaws.com/ukstationliveimg/download.png)](https://s3-eu-west-1.amazonaws.com/ukstationlive/stations.json)


<h2>Huxley</h2>
![Huxley Icon](https://raw.githubusercontent.com/OliPicard/Huxley/master/src/Huxley/huxley.png)

[Huxley](https://github.com/jpsingleton/Huxley/) is a SOAP proxy client that reduces the headaches educed by the national rail XML SOAP system.

<h2>Cupid</h2>
[Cupid](https://github.com/OliPicard/cupid/blob/master/cupid.py) is a simple csv to json tool written with the national rail station codes in mind. built with the help of the community, the converter helps us push out updates faster than ever.


![Powered By National  Rail](https://raw.githubusercontent.com/OliPicard/Huxley/master/src/Huxley/NRE_Powered_logo.png)

[National Rail API](http://realtime.nationalrail.co.uk/OpenLDBWSRegistration)

<h2>Credits</h2>
Developed with love by [OliPicard](http://github.com/olipicard)

a massive thank you goes out to the following individuals and groups.

/r/LearnPython - for your help during tough times!

James Singleton - for developing Huxley (saved me many hours)

diminonten - for the in memory cupid editor

wub_wub - for putting up with my silly questions.

__love__ - for helping me understand that global isn't the right place to store code.

excalibur - for putting up with my streaming requests and providing me example code to work with to implement cupid.

<h3> License </h3>
The UKStationLive app is open sourced under the GNU GPL 3.0 License (Provided inside the Git Repo)

THIS PROGRAM HAS ABOSLUTELY NO WARRENTY

![GNU GPL 3.0](http://www.gnu.org/graphics/gplv3-127x51.png)
