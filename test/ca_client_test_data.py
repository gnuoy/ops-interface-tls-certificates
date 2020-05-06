# Copyright 2020 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import yaml


def get_yaml_test_data(file_name):
    with open('./test/{}'.format(file_name), 'r') as data_file:
        test_data = yaml.load(data_file, Loader=yaml.SafeLoader)
    return test_data


def get_multi_rq_relation_data_server():
    return get_yaml_test_data('multi_cert_rel_test_data_server.yaml')


def get_multi_rq_relation_data_client():
    return get_yaml_test_data('multi_cert_rel_test_data_client.yaml')


TEST_RELATION_DATA = {
    'ca': '''-----BEGIN CERTIFICATE-----
MIIDVDCCAjygAwIBAgIUQO166wG7dRB41Czxex8Xd+7HlVMwDQYJKoZIhvcNAQEL
BQAwGTEXMBUGA1UEAwwOMTAuMjA5LjI0MC4xNzYwHhcNMjAwNDAyMTAwNDU5WhcN
MzAwMzMxMTAwNDU5WjAZMRcwFQYDVQQDDA4xMC4yMDkuMjQwLjE3NjCCASIwDQYJ
KoZIhvcNAQEBBQADggEPADCCAQoCggEBAKi+UWiQaNKIFkjVoBzxMdTWDaYXmoEY
zIu12zzIyQUisTa9ASEgCaY0OyJYauwwN20LvjLhMVf1stIXVwewxiIuiFm1s8sA
1xUiIKZOOLWiTWyUGhtNdi2augGnZNXRCzBEsGLkys/kJdwhpqhfqnt/9eCa6fuD
ajUkl43he/fjdF1EF1HLlGZm7QHo4XHODX2GFYAmRH/2F7iJeUDEAZ4mltFMNEvx
hCMvV+mCTp6ZJAye+1Ld1gndsO0v9bgAWfE4CZoZx4+PgDm5ylxFZqYWvTrPfkb3
dul6Ga2m1TI7U5Cct7oTgrOBjxrZSpkP6eRMLsQ0QM2yujNV7mpD9OsCAwEAAaOB
kzCBkDAdBgNVHQ4EFgQU4DvugbL1p9yCrCYIWIE1CbnS6EYwVAYDVR0jBE0wS4AU
4DvugbL1p9yCrCYIWIE1CbnS6EahHaQbMBkxFzAVBgNVBAMMDjEwLjIwOS4yNDAu
MTc2ghRA7XrrAbt1EHjULPF7Hxd37seVUzAMBgNVHRMEBTADAQH/MAsGA1UdDwQE
AwIBBjANBgkqhkiG9w0BAQsFAAOCAQEAEYvAm+DFQuQqrEbVnlzXMySN57K1f6j9
xN7FJHoe2pn1At1/skdpQlxCozNzXtCHHfzfd2qoxxHZMDTIHJzZyWjGez02jPTZ
NBpYJ2PxZPtvQS5V8Q++7pqVlTwTRhRbEuyqGYDBBixpu2zgda0myQpaYguSIrjb
9bGeQZ4iBP8SjXCxksVQmrGNTE+/ooP/L/e9Jn0f/jOOkJfMKmgAO3PJW03sSwJK
vLkurCsHpRm9JzImcopKb+dRBQem9ap74Ab9QX7rUzkH5IKJwjk+wp9fBs9beQBA
/topCU469e0vh/yNjo1/h+bdXMWebv4HNAiXPdp6Yi7VohTtyHz2VA==
-----END CERTIFICATE-----''',
    'myserver_0.server.cert': '''Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 2 (0x2)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=10.209.240.176
        Validity
            Not Before: Apr  2 10:05:27 2020 GMT
            Not After : Mar 31 10:05:27 2030 GMT
        Subject: CN=juju-b39c76-0.lxd
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:ce:dc:f5:e8:3e:47:5f:4d:76:0e:06:bf:d6:66:
                    05:6f:6b:4c:84:c1:84:1c:a5:86:16:29:06:ba:bf:
                    16:27:bf:86:08:95:4d:98:73:a9:3b:17:90:05:b0:
                    1d:ec:d9:4c:1f:c6:12:5d:a7:78:cb:d9:35:7d:25:
                    4d:c6:58:f8:4c:2b:92:d9:46:f6:3d:44:2c:6c:bc:
                    04:87:ad:25:16:99:41:c9:79:72:12:2b:88:5c:21:
                    01:70:d0:c9:b5:d9:97:2d:55:96:bc:bd:8c:29:3c:
                    3c:17:33:06:ff:97:2b:1d:5f:65:ca:43:56:19:68:
                    15:6e:f2:99:ee:f0:e7:fd:fc:5e:d3:5a:73:e8:2e:
                    c4:cd:83:31:b4:e0:c6:f7:6a:46:a7:8d:56:08:1d:
                    bf:f4:fa:ff:a7:4c:11:6f:06:7b:94:14:d3:fa:a1:
                    2b:ad:88:1a:5e:03:05:c4:7f:74:11:5c:04:b4:96:
                    ed:b6:77:2a:71:8c:e5:2f:7c:50:0c:0b:57:c6:56:
                    f5:2b:5a:ae:ea:7e:f4:63:0d:3d:74:81:e6:38:38:
                    7d:6c:4c:20:0f:2c:29:13:5f:66:b8:1a:ea:d3:1d:
                    31:1c:be:09:04:73:5e:aa:14:08:30:55:94:28:fe:
                    d8:00:04:62:d6:1b:42:c1:92:d5:6d:d5:18:c0:72:
                    67:a9
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints:
                CA:FALSE
            X509v3 Subject Key Identifier:
                E3:92:29:36:3F:EC:74:94:A8:BE:2E:01:A7:4B:E3:BE:37:EE:71:F6
            X509v3 Authority Key Identifier:
                keyid:E0:3B:EE:81:B2:F5:A7:DC:82:AC:26:08:58:81:35:09:B9:D2:E8:46
                DirName:/CN=10.209.240.176
                serial:40:ED:7A:EB:01:BB:75:10:78:D4:2C:F1:7B:1F:17:77:EE:C7:95:53

            X509v3 Extended Key Usage:
                TLS Web Client Authentication, TLS Web Server Authentication
            X509v3 Key Usage:
                Digital Signature, Key Encipherment
            X509v3 Subject Alternative Name:
                IP Address:10.209.240.236, DNS:juju-b39c76-0.lxd
    Signature Algorithm: sha256WithRSAEncryption
         6e:46:05:bb:50:5c:ef:45:63:0a:e1:ba:59:aa:f4:47:cd:8c:
         a3:0c:52:0d:e4:ee:4a:8d:12:6c:32:e8:99:09:3b:39:a2:bf:
         45:b4:06:6f:c6:d1:fb:3d:b0:d8:b2:6d:51:2d:99:39:20:95:
         07:e5:13:89:d6:5f:20:ec:d6:31:c6:1e:ae:c9:59:e8:70:0b:
         ce:ba:7d:e0:b9:22:73:15:2e:31:29:55:4d:a1:b4:3d:6c:fd:
         25:96:0e:4f:a1:d9:fb:f1:c4:4a:54:09:35:57:87:5b:1a:b8:
         db:e1:e5:88:4e:6f:c7:d5:55:fd:39:c7:c8:43:ce:c9:7d:5f:
         6d:76:01:25:d7:32:d4:d7:30:93:25:04:78:b6:c5:05:aa:62:
         25:33:a0:82:34:9a:01:10:15:ee:75:c5:5b:12:e2:a4:11:27:
         82:e9:f2:db:37:b7:dd:33:ed:e9:2a:2e:2c:b9:65:71:f8:98:
         e2:53:b6:30:6d:2b:ab:70:71:a2:b7:ce:6b:fd:1e:be:14:9b:
         33:77:13:37:a3:61:80:0a:54:21:2e:37:ec:af:e8:17:50:1d:
         09:a2:63:c9:2a:91:e9:8c:a4:4b:eb:4f:01:b2:3a:9a:15:06:
         63:a0:c0:ff:51:95:d8:8f:1d:c3:31:83:39:c5:2a:f7:95:f6:
         26:76:fd:20
-----BEGIN CERTIFICATE-----
MIIDhDCCAmygAwIBAgIBAjANBgkqhkiG9w0BAQsFADAZMRcwFQYDVQQDDA4xMC4y
MDkuMjQwLjE3NjAeFw0yMDA0MDIxMDA1MjdaFw0zMDAzMzExMDA1MjdaMBwxGjAY
BgNVBAMMEWp1anUtYjM5Yzc2LTAubHhkMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEAztz16D5HX012Dga/1mYFb2tMhMGEHKWGFikGur8WJ7+GCJVNmHOp
OxeQBbAd7NlMH8YSXad4y9k1fSVNxlj4TCuS2Ub2PUQsbLwEh60lFplByXlyEiuI
XCEBcNDJtdmXLVWWvL2MKTw8FzMG/5crHV9lykNWGWgVbvKZ7vDn/fxe01pz6C7E
zYMxtODG92pGp41WCB2/9Pr/p0wRbwZ7lBTT+qErrYgaXgMFxH90EVwEtJbttncq
cYzlL3xQDAtXxlb1K1qu6n70Yw09dIHmODh9bEwgDywpE19muBrq0x0xHL4JBHNe
qhQIMFWUKP7YAARi1htCwZLVbdUYwHJnqQIDAQABo4HTMIHQMAkGA1UdEwQCMAAw
HQYDVR0OBBYEFOOSKTY/7HSUqL4uAadL47437nH2MFQGA1UdIwRNMEuAFOA77oGy
9afcgqwmCFiBNQm50uhGoR2kGzAZMRcwFQYDVQQDDA4xMC4yMDkuMjQwLjE3NoIU
QO166wG7dRB41Czxex8Xd+7HlVMwHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUF
BwMBMAsGA1UdDwQEAwIFoDAiBgNVHREEGzAZhwQK0fDsghFqdWp1LWIzOWM3Ni0w
Lmx4ZDANBgkqhkiG9w0BAQsFAAOCAQEAbkYFu1Bc70VjCuG6War0R82MowxSDeTu
So0SbDLomQk7OaK/RbQGb8bR+z2w2LJtUS2ZOSCVB+UTidZfIOzWMcYerslZ6HAL
zrp94LkicxUuMSlVTaG0PWz9JZYOT6HZ+/HESlQJNVeHWxq42+HliE5vx9VV/TnH
yEPOyX1fbXYBJdcy1NcwkyUEeLbFBapiJTOggjSaARAV7nXFWxLipBEnguny2ze3
3TPt6SouLLllcfiY4lO2MG0rq3BxorfOa/0evhSbM3cTN6NhgApUIS437K/oF1Ad
CaJjySqR6YykS+tPAbI6mhUGY6DA/1GV2I8dwzGDOcUq95X2Jnb9IA==
-----END CERTIFICATE-----
    ''',
    'myserver_0.server.key': '''-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDO3PXoPkdfTXYO
Br/WZgVva0yEwYQcpYYWKQa6vxYnv4YIlU2Yc6k7F5AFsB3s2UwfxhJdp3jL2TV9
JU3GWPhMK5LZRvY9RCxsvASHrSUWmUHJeXISK4hcIQFw0Mm12ZctVZa8vYwpPDwX
Mwb/lysdX2XKQ1YZaBVu8pnu8Of9/F7TWnPoLsTNgzG04Mb3akanjVYIHb/0+v+n
TBFvBnuUFNP6oSutiBpeAwXEf3QRXAS0lu22dypxjOUvfFAMC1fGVvUrWq7qfvRj
DT10geY4OH1sTCAPLCkTX2a4GurTHTEcvgkEc16qFAgwVZQo/tgABGLWG0LBktVt
1RjAcmepAgMBAAECggEAG1Jz6EjRhHTmstORYu/2p9C0OpSUrnPuUd75VJEIjBdv
zJJrvUcJgxSJoTaxvSa2NzwiENydx87Ykb7rltcJdIYMz0XgIBdxBquOrZzg2StE
1SeFOYEmcYSqfAwXmD01CnfTgPpIGOorxaSnt/pvZ2HCQATEynZE3nKMglKvUYxW
yBcepz4Ub/FfiLDsIwmqmdeKISTIzryC+aw2P7W74kjDW8qyY0G50od4gx8He767
lAtkrj3XA5mXw0s1JuTDAQUVKFum1/yCzntt3zn8huP9QbX/vOxkw+BzxRa7WHvH
PoHr8lwxKr8ImKu2xIMGJueRsq9YgdjGHDTRKjUFAQKBgQD3Ku9GnF/6ntcit79x
DJ3YSvLpkZYgIIA+mFCFLHBDbQgNe2Qy9CFgmKSuYuDSS9NHWWPdHkNsK8jdcrXm
H7VosfrCgnmXHzZ7KupnioTGBSdynCRdtZB6QktlW1lX86mdeX2VKveJTfENKHlI
6xOOn2qeG+rT8LyqQ9oOS5TqLQKBgQDWQVLYK0D1TUIT5XTy5tdibZM1ULTBy838
f6CyPI3VBF54wgQ93yKr7CHrLdFsdG74bIBpRVFmNxQjRmNEAVYdSCw44w8ESQ3z
c8+pHkgEQT9K/9ocpPYDgtihI6ltg3C+3iFisBMnBJbQsDEDTyNIIycADAWDmehj
U8WlsbmM7QKBgGumx5B5i1Qc2pbEcR1L4XPTMPmJ71kOzsx0ip12PW8gjeFRXNLU
gbUQxqktZ74wSFVLGbO0+qiiaVoKHC+en+R5oD4Xld28On5qsq1mJ24X0Jaaazxl
WAfn1+7NWpx0A+wSfh/6FtY2nEae2jRoLpxv0oAKqLymnYWLB+4x/SoBAoGBAJWF
cPM6/FI0YHDSKRN61cTzA1CpyfuU52PXDaZVbAXEzsknXR5wohmo6OLfTs+JUgg8
cEEHBw92UK9tZ8kFxbsZqwLoMoqjEQFdSQaVA100y57jfquO08EPh26tHIg4um35
RwNALZ2FLlrlGs9cYxrsrULzIMX+mpb213AS35LhAoGBAOP3z3qcmh++V6MFO/iB
rl7o+5GYIbYUREbtgQMyjzze6QLg/YKulS5PTkkk82AzSOEbyPPfAO/iQj6LQyJg
A5+kCuEFo5NKPMyeKopxN78ncLbe01IdFn+MvJBLMU6GRAaezsoR3c1ywu1ptp3S
pg4Y/1rKERj5uyDqRWyCIb2k
-----END PRIVATE KEY-----'''
}
