# Redis Introduction

## What is Redis?

Redis (Remote Dictionary Server) is an open-source, in-memory data structure store that can be used as a database, cache, message broker, and streaming engine. It supports various data structures such as strings, hashes, lists, sets, sorted sets, streams, hyperloglogs, bitmaps, and spatial indexes.

## Key Features

- **In-memory storage**: Redis keeps all data in RAM, which makes it extremely fast
- **Persistence options**: Can save data to disk periodically or log operations for durability
- **Data structures**: Supports complex data structures beyond simple key-value pairs
- **Atomic operations**: Provides atomic operations on these data types
- **Pub/Sub messaging**: Built-in publish/subscribe messaging paradigm
- **Lua scripting**: Supports server-side scripting with Lua
- **Transactions**: Allows execution of a group of commands in a single step
- **Replication**: Master-slave replication for high availability
- **Cluster mode**: Horizontal scaling with automatic sharding

## Common Use Cases

- **Caching**: Store frequently accessed data to reduce database load
- **Session storage**: Manage user sessions in web applications
- **Real-time analytics**: Count and track events in real-time
- **Leaderboards/counting**: Implement sorted sets for rankings
- **Message queues**: Use lists for lightweight queue implementation
- **Rate limiting**: Control API usage and prevent abuse
- **Geospatial applications**: Store and query location-based data

## Basic Redis Commands

```
# String operations
SET key value
GET key

# Hash operations
HSET key field value
HGET key field

# List operations
LPUSH key value
RPOP key

# Set operations
SADD key member
SMEMBERS key

# Sorted set operations
ZADD key score member
ZRANGE key start stop

# Key operations
EXISTS key
DEL key
EXPIRE key seconds
```

## Redis Data Types

1. **Strings**: Binary-safe strings up to 512MB in size
2. **Lists**: Linked lists of string values
3. **Sets**: Unordered collections of unique strings
4. **Sorted Sets**: Sets ordered by a score value
5. **Hashes**: Maps of field-value pairs
6. **Streams**: Append-only collections of map-like entries
7. **Bitmaps**: String values treated as bit arrays
8. **HyperLogLogs**: Probabilistic data structure for counting unique elements
9. **Geospatial indexes**: Store and query points by geographic location

## Redis Persistence

Redis offers several persistence options:

- **RDB (Redis Database)**: Point-in-time snapshots at specified intervals
- **AOF (Append Only File)**: Logs every write operation
- **Hybrid approach**: Combines both RDB and AOF

## Redis Replication

Redis supports master-slave replication where data from a master server is copied to one or more replica servers. This provides:

- Data redundancy
- Improved read performance (by distributing read operations)
- Disaster recovery capabilities

## Redis Cluster

Redis Cluster provides:

- Automatic data sharding across multiple Redis nodes
- High availability during partitions
- Linear scalability up to 1000 nodes

## Redis Security

Redis security features include:

- Password authentication
- SSL/TLS encryption (in newer versions)
- Access control lists (ACLs) for fine-grained access control
- Protected mode for network security

## Redis Modules

Redis can be extended with modules that add new data types and capabilities:

- **RediSearch**: Full-text search engine
- **RedisJSON**: Native JSON support
- **RedisTimeSeries**: Time-series data structure
- **RedisGraph**: Graph database implementation
- **RedisBloom**: Probabilistic data structures

## Redis vs. Other Databases

- **Redis vs. Memcached**: Redis offers more data structures and persistence
- **Redis vs. MongoDB**: Redis is in-memory and simpler, MongoDB is document-oriented
- **Redis vs. PostgreSQL**: Redis is NoSQL and in-memory, PostgreSQL is a relational database

## Redis Limitations

- Memory constraints (data size limited by available RAM)
- Single-threaded architecture (though Redis 6 introduced threaded I/O)
- Limited query capabilities compared to relational databases
- Eventual consistency in distributed setups