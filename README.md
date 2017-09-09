## Synopsis

This project provides a 3D Virtual Reality environment that represents the Smart Home Living Lab UPM and it also allows to control the different devices  by using the HTTP protocol. To established the connection between the server (3D Living Lab Software Vizard WorldViz) and the client (any browser EG. Chrome, Mozilla Firefox, Safari, etc), it is used the REST web architecture.

## Motivation

The aim of the project is to represent  and to control the environment and the devices of the 3D Virtual Reality Smart Home Living Lab UPM. 

## Minimum Requirements

1. A computer with Windows Operating System: 

    - Window XP SP3 or above

    - Pentium processor at 1 GHz or higher (Recommended: Dual Core 2 GHz or higher)

    - OpenGL compatible graphics card (Recommended: nVidia GeForce 6 series with 128 MB or greater)

    - 1 GB RAM (Recommended: 2 GB RAM or greater)

    - 400 MB hard drive space

2. Internet Connection




## Installation

For the installation download the executable [.exe](https://owncloud.lst.tfo.upm.es/index.php/s/hjjVTTbmOxf7SEn) and just install it in your computer.
Also If you have Vizard WorldViz program installed in your computer, you can  clone the repository from this [url](https://gitlab.lst.tfo.upm.es/Plan4Act/3D_Virtual_Living_Lab.git) and run CODIGO_TFG_ALBA_GET_Y_SET_VERSION_INGLES.py in Vizard.  

Then you will see the next screen which shows a view of the main door and the IP direction:
<p align="center">
  <img src="https://fotos.subefotos.com/8f358e5de887432a5374bfce7953219co.jpg" />
</p>

## Client and Server communication

In this project two different operations are implemented:
- To change the device state
- To ask for a device state

The requests to Server may be performed with HTTP GET or POST. 

Below in **Table 1** are the different values that the parameter "device" can have and the appliance to which they represent:

 ### Table 1 <a id="table1"></a>

| Device                | Device value       |
| ----------            | ----------         | 
| Doorstep              | doorHome           |
| Livingroom door       | doorSalon          |
| Bathroom door         | doorBath           |
| Kitchen door          | doorKitchen        |
| Bedroom blind         | RollupBed          |
| Kitchen blind         | RollupKit          |
| Livingroom blind      | RollupSal          |
| Kitchen light         | KitchenLight       |
| Livingroom light      | SalaLight          |
| Bedroom light         | BedroomLight       |
| Bathroom light        | BathroomLight      |
| Control room light    | SCLight            |
| RV room light         | RVLight            |
| Control room blind    | RollupSC           |
| Control room door     | doorSC             |



 - GET: In GET requests the parameters are sent in the querystring, these parameters are the comand ("cmd"), the name of the device ("device") and the new state that you want of the device ("state"). Following there are two explamples:

   - Change the device state: It is necessary to indicate that the *cmd* parameter is "set_status", the *device* (One of the device values of the second column of the [Table 1](#table1)), the *device_id* that is always 1 and the new *status* which can be "open" or "close". 

      EG : **"http://192.168.1.12:8080/vizhtml/custom_handler/?cmd=set_status&device_id=1&device=doorHome&state=open"**

   - Request for the device state: It is necessary to indicate that the cmd parameter is "get_status" and the device. 

      EG : **"http://192.168.1.12:8080/vizhtml/custom_handler/?cmd=get_status&device_id=1&device=doorHome&state=open"**

 - POST: In POST request the parameters are sent in the request body as text, these parameters are only the device which you can change ("device") and the new state ("state") of it, with POST request you can only change the device state.

    EG : **"http://192.168.1.12:8080/vizhtml/custom_handler/"** into the body the format request is **cmd=get_status&device_id=1&device=doorHome&state=open**

 When the GET or POST request are made the server response with a JSON object with the parameters:

 - version : which is always mercury.
 - cmd : which shows the command (set_status or get_status).
 - code_ : which shows if in the request the enter device is wrong (404), if the enter state is wrong (405) or if the request is correct (201).
 - description : Shows the request error (Change device value or Change state value).
 - device_id : Shows the device identifier which is a number.
 - device_name : Shows the device name.
 - value : Shows the state of the device.
 - status: Shows if the request is correct ("OK") or incorrect ("FAILURE").

An example of the JSON string:
```json
{"version":"mercury","cmd":"set_status","code":"404","description":"Change device value.","device_id":"1","device_name":"RVLightd","value":"close","status":"FAILURE"}
```

You need to know the IP direction of the computer where the 3D Living Lab executable is running in order to use it in the url of the HTTP request used to connect the client with the server.




Please note that:

 > The server and the client have to work on the same network or the server has to be visible by the client. Take also care that no firewalls are blocking the HTTP and HTTPS ports. It has been tested in these use cases:
 - Vizard server is a WiFi Hotspot and client is connected to it.
 


## Code Example

For doing a GET request:

```typescript
public getJsonData(url): Promise<String> {
    return this.http.get(url)
      .toPromise()
      .then(response => response.json() as Object)
      .catch(this.handleError);
  }        

this.dataService.getJsonData('http://' + this.ipRV + ':8080/vizhtml/custom_handler/?cmd=set_status&device_id=1&' + otro.url_close);
```
 

You need to define in the code the parameters of the url:
 - IP Direction of the computer where the Server is executed on.
 - Port is always 8080 (established by Vizard WorldViz).
 - The device and the device state.
 - Cmd which can be set_status or get_status.       

The "url" is of the following type:

**'http://192.168.2.12:8080/vizhtml/custom_handler/?cmd=set_status&device_id=1&device=doorKitchen&state=open/'**      			 


## API Reference

See comments into *```CODIGO_TFG_ALBA_GET_Y_SET_VERSION_INGLES.py```* file. 


## Contributors

- Eugenio Gaeta (UPM)
- Alba M. Gallego Montejo (UPM)

## License

MIT License

Copyright (c) [2017] [Universidad Politecnica de Madrid]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.