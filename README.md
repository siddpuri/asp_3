# TEMPORARY TODO/NOTES LIST
### im adding this because i need to not forget to do these things
#### plus its helpful if you guys know this too

- based on the new framework for handling networking, each server->client payload *with the exception of physics packets and the initial client_id message* must be a **serialized json object** in the following format:

```typescript
{
    type: str // basically an event name. When the client registers an event using socket_man.on(event_name, ...), this should be the event_name.
    data: any // the data to be sent to the client. This can be anything, but it must be serializable.
}
```

## ANOTHER IMPORTANT NOTE
Please use `GameManager.socket_man.socket.close()` on every `pygame.QUIT` event. This will close the socket connection gracefully and prevent a ghost client instance on the server.