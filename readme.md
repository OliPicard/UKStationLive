<h1>UKStationLive</h1>
UKStationLive is a live endpoint client powered by [Huxley](https://github.com/jpsingleton/Huxley/) and National Rail's live Darwin Service. The client is open sourced under the GPL 3.0 free software license.

Using the Cloud (S3) to pull station CRS codes, grab data from the JSON station Huxley service (Azure) and provide a multiplatform experience. Simply put this app allows you to view when trains will be arriving at a platform, What platform they are arriving from, The origin of the train and the final destination of the train.


<h2>Requirements</h2>
Requests Module (pip install requests)
[Huxley](https://github.com/jpsingleton/Huxley/wiki/Hosting-Quick-Start)
[Python 3](http://python.org)
[National Rail API key](http://realtime.nationalrail.co.uk/OpenLDBWSRegistration) - Please use your own API key.
Access to the internet.

<h2>Station CSRs</h2>
We are currently porting over data from the National Rail Station code service to JSON.

Updates are occurring to the station CSR code file every 2-3 days, these happen in the background over S3 and are pushed to the client over the air. a local copy of the station CSR file will be released in the future.

<h2>Huxley</h2>
![Huxley Icon](https://raw.githubusercontent.com/OliPicard/Huxley/master/src/Huxley/huxley.png)
Huxley is a SOAP proxy client that reduces the headaches educed by the national rail XML SOAP system.
![Powered By National  Rail]()

<h2>Credits</h2>
Developed with love by [OliPicard](http://github.com/olipicard)

a massive thank you goes out to the following individuals and groups.

/r/LearnPython - for your help during tough times!

James Singleton - for developing Huxley (saved me many hours)
