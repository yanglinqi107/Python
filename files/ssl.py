import ssl
import aiohttp
import asyncio


async def test():
    FORCED_CIPHERS = (
        'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
        'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES'
    )
    sslcontext = ssl.create_default_context()
    sslcontext.options |= ssl.OP_NO_SSLv3
    sslcontext.options |= ssl.OP_NO_SSLv2
    sslcontext.options |= ssl.OP_NO_TLSv1_1
    sslcontext.options |= ssl.OP_NO_TLSv1_2
    sslcontext.options |= ssl.OP_NO_TLSv1_3
    sslcontext.set_ciphers(FORCED_CIPHERS)

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=50, loop=loop)) as session:
        # r = await session.get('https://www.mdnkids.com/news/?Serial_NO=108552', ssl=sslcontext)
        r = await session.get('http://www.diyibanzhuvip9.xyz/27/27152/675578.html', proxy="http://118.135.217.7:80", ssl=sslcontext)
        print(await r.text())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())