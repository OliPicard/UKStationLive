<h1>UKStationLive</h1>
![ukstationlive](https://s3-eu-west-1.amazonaws.com/ukstationliveico/ukstationlivepub.png)

UKStationLive is a live endpoint client powered by [Huxley](https://github.com/jpsingleton/Huxley/) and National Rail's live Darwin Service. The client is open sourced under the GPL 3.0 free software license.

Using the Cloud (S3) to pull station CRS codes, grab data from the JSON station Huxley service (Azure) and provide a multiplatform experience. Simply put this app allows you to view when trains will be arriving at a platform, What platform they are arriving from, The origin of the train and the final destination of the train.


<h2>Requirements</h2>
[Requests](http://docs.python-requests.org/en/latest/) Module (pip install requests)

[Huxley](https://github.com/jpsingleton/Huxley/wiki/Hosting-Quick-Start)

[Python 3](http://python.org)

[National Rail API key](http://realtime.nationalrail.co.uk/OpenLDBWSRegistration) - Please use your own API key.
Access to the internet.

<h2>Setup</h2>
edit the config.json file in your own text editor, We personally <3 [Atom](http://atom.io)

Be sure to replace the following items.

1) The Huxley Proxy url with your own Huxley proxy.
2) The API key. See above for the National Rail API key URL.

<h2>Station CSRs</h2>
We are currently porting over data from the National Rail Station code service to JSON.

Updates are occurring to the station CSR code file every 2-3 days, these happen in the background over S3 and are pushed to the client over the air. a local copy of the station CSR file will be released in the future.


<h2>Huxley</h2>
![Huxley Icon](https://raw.githubusercontent.com/OliPicard/Huxley/master/src/Huxley/huxley.png)

[Huxley](https://github.com/jpsingleton/Huxley/) is a SOAP proxy client that reduces the headaches educed by the national rail XML SOAP system.


![Powered By National  Rail](https://raw.githubusercontent.com/OliPicard/Huxley/master/src/Huxley/NRE_Powered_logo.png)

[National Rail API](http://realtime.nationalrail.co.uk/OpenLDBWSRegistration)

<h2>Credits</h2>
Developed with love by [OliPicard](http://github.com/olipicard)

a massive thank you goes out to the following individuals and groups.

/r/LearnPython - for your help during tough times!

James Singleton - for developing Huxley (saved me many hours)

<h3> License </h3>
The UKStationLive app is open sourced under the GNU GPL 3.0 License (Provided inside the Git Repo)

THIS PROGRAM HAS ABOSLUTELY NO WARRENTY

![GNU GPL 3.0](http://www.gnu.org/graphics/gplv3-127x51.png)
