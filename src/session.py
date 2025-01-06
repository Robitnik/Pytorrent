import libtorrent as lt

class Session:
    """
    Represents a torrent session using libtorrent. Manages session settings, rate limits,
    network interfaces, and provides methods to interact with the torrent ecosystem.
    """

    def __init__(self, 
                 libtorrent=lt, 
                 user_agent="Python client v1.0.0",
                 listen_interfaces="0.0.0.0", 
                 port=6881,
                 download_rate_limit=0,
                 upload_rate_limit=0,
                 session=None) -> None:
        """
        Initializes the Session object with default or specified parameters.

        Args:
            libtorrent: The libtorrent library instance.
            user_agent (str): The user agent string identifying the client.
            listen_interfaces (str): Network interfaces to listen on.
            port (int): Port number for incoming connections.
            download_rate_limit (int): Download rate limit in KB/s. 0 for unlimited.
            upload_rate_limit (int): Upload rate limit in KB/s. 0 for unlimited.
            session: Existing libtorrent session object. If None, a new session is created.
        """
        self._user_agent = user_agent
        self._listen_interfaces = listen_interfaces
        self._port = port
        self._download_rate_limit = download_rate_limit
        self._upload_rate_limit = upload_rate_limit
        self._lt = libtorrent
        self._session = session or self.create_session()

    def create_session(self):
        """
        Creates a new libtorrent session with the specified listen interfaces and port.

        Returns:
            libtorrent.session: The created libtorrent session object.
        """
        self._session = self._lt.session({'listen_interfaces': f'{self._listen_interfaces}:{self._port}'})
        return self._session

    def set_download_limit(self, rate=0):
        """
        Sets the download rate limit for the session.

        Args:
            rate (int): Download rate limit in KB/s. 
                        -1 for minimal rate, 0 for unlimited, positive integers for specific limits.
        """
        self._download_rate_limit = int(-1 if rate == 0 else (1 if rate == -1 else rate * 1024))
        self._session.set_download_rate_limit(self._download_rate_limit)
        return self._download_rate_limit

    def set_upload_limit(self, rate=0):
        """
        Sets the upload rate limit for the session.

        Args:
            rate (int): Upload rate limit in KB/s. 
                        -1 for minimal rate, 0 for unlimited, positive integers for specific limits.
        """
        self._upload_rate_limit = int(-1 if rate == 0 else (1 if rate == -1 else rate * 1024))
        self._session.set_upload_rate_limit(self._upload_rate_limit)
        return self._upload_rate_limit

    def get_upload_limit(self):
        """
        Retrieves the current upload rate limit.

        Returns:
            int: The upload rate limit in bytes per second.
        """
        return self._session.upload_rate_limit()

    def get_download_limit(self):
        """
        Retrieves the current download rate limit.

        Returns:
            int: The download rate limit in bytes per second.
        """
        return self._session.download_rate_limit()

    def __str__(self):
        """
        Returns a human-readable string representation of the session.

        Returns:
            str: String representation of the session.
        """
        return f"Session(user_agent={self._user_agent}, listen_interfaces={self._listen_interfaces}, port={self._port})"

    def __repr__(self):
        """
        Returns an unambiguous string representation of the session.

        Returns:
            str: Detailed string representation of the session.
        """
        return (f"Session(user_agent={self._user_agent!r}, listen_interfaces={self._listen_interfaces!r}, "
                f"port={self._port!r}, download_rate_limit={self._download_rate_limit!r}, "
                f"upload_rate_limit={self._upload_rate_limit!r})")

    def __call__(self):
        """
        Allows the session object to be called to create a new session.

        Returns:
            libtorrent.session: The created libtorrent session object.
        """
        return self.create_session()

    # Additional Methods

    def add_dht_node(self, node):
        """
        Adds a DHT node to the session.

        Args:
            node (tuple): A tuple containing the IP address and port of the DHT node.
        """
        self._session.add_dht_node(node)
        return True  # Indicate success

    def add_dht_router(self, router):
        """
        Adds a DHT router to the session.

        Args:
            router (tuple): A tuple containing the IP address and port of the DHT router.
        """
        self._session.add_dht_router(router)
        return True  # Indicate success

    def add_extension(self, extension):
        """
        Adds an extension to the session.

        Args:
            extension: The extension to add.
        """
        self._session.add_extension(extension)
        return True  # Indicate success

    def add_port_mapping(self, mapping):
        """
        Adds a port mapping to the session.

        Args:
            mapping: The port mapping to add.
        """
        self._session.add_port_mapping(mapping)
        return True  # Indicate success

    def add_torrent(self, torrent_info):
        """
        Adds a torrent to the session.

        Args:
            torrent_info: The torrent information to add.

        Returns:
            lt.torrent_handle: The handle to the added torrent.
        """
        return self._session.add_torrent(torrent_info) 

    def apply_settings(self, settings):
        """
        Applies settings to the session.

        Args:
            settings: A dictionary of settings to apply.
        """
        self._session.apply_settings(settings)
        return True  # Indicate success

    def async_add_torrent(self, torrent_info):
        """
        Asynchronously adds a torrent to the session.

        Args:
            torrent_info: The torrent information to add.

        Returns:
            lt.torrent_handle: The handle to the added torrent.
        """
        torrent_handle = self._session.async_add_torrent(torrent_info)
        return torrent_handle

    def create_peer_class(self, peer_class):
        """
        Creates a new peer class.

        Args:
            peer_class: The peer class to create.
        """
        self._session.create_peer_class(peer_class)
        return True  # Indicate success

    def delete_files(self, torrent_handle):
        """
        Deletes the files associated with a torrent.

        Args:
            torrent_handle: The handle of the torrent whose files are to be deleted.
        """
        self._session.delete_files(torrent_handle)
        return True  # Indicate success

    def delete_partfile(self, torrent_handle):
        """
        Deletes the partfile associated with a torrent.

        Args:
            torrent_handle: The handle of the torrent whose partfile is to be deleted.
        """
        self._session.delete_partfile(torrent_handle)
        return True  # Indicate success

    def delete_peer_class(self, peer_class_id):
        """
        Deletes a peer class by its ID.

        Args:
            peer_class_id (int): The ID of the peer class to delete.
        """
        self._session.delete_peer_class(peer_class_id)
        return True  # Indicate success

    def delete_port_mapping(self, mapping):
        """
        Deletes a port mapping from the session.

        Args:
            mapping: The port mapping to delete.
        """
        self._session.delete_port_mapping(mapping)
        return True  # Indicate success

    def dht_announce(self, info_hash, port):
        """
        Announces to the DHT that a torrent is being seeded.

        Args:
            info_hash: The info hash of the torrent.
            port (int): The port number to announce.
        """
        self._session.dht_announce(info_hash, port)
        return True  # Indicate success

    def dht_get_immutable_item(self, info_hash):
        """
        Retrieves an immutable item from the DHT.

        Args:
            info_hash: The info hash of the torrent.

        Returns:
            The immutable item retrieved from the DHT.
        """
        item = self._session.dht_get_immutable_item(info_hash)
        return item

    def dht_get_mutable_item(self, key):
        """
        Retrieves a mutable item from the DHT.

        Args:
            key: The key of the mutable item.

        Returns:
            The mutable item retrieved from the DHT.
        """
        item = self._session.dht_get_mutable_item(key)
        return item

    def dht_get_peers(self, info_hash):
        """
        Retrieves peers for a torrent from the DHT.

        Args:
            info_hash: The info hash of the torrent.

        Returns:
            list: List of peers retrieved from the DHT.
        """
        peers = self._session.dht_get_peers(info_hash)
        return peers

    def dht_live_nodes(self):
        """
        Retrieves the live nodes in the DHT.

        Returns:
            list: List of live DHT nodes.
        """
        nodes = self._session.dht_live_nodes()
        return nodes

    def dht_proxy(self, proxy):
        """
        Sets the DHT proxy.

        Args:
            proxy: The proxy to set for DHT.
        """
        self._session.dht_proxy(proxy)
        return True  # Indicate success

    def dht_put_immutable_item(self, info_hash, data):
        """
        Puts an immutable item into the DHT.

        Args:
            info_hash: The info hash of the torrent.
            data: The data to store.
        """
        self._session.dht_put_immutable_item(info_hash, data)
        return True  # Indicate success

    def dht_put_mutable_item(self, key, value):
        """
        Puts a mutable item into the DHT.

        Args:
            key: The key of the mutable item.
            value: The value to store.
        """
        self._session.dht_put_mutable_item(key, value)
        return True  # Indicate success

    def dht_sample_infohashes(self, count):
        """
        Samples a number of infohashes from the DHT.

        Args:
            count (int): The number of infohashes to sample.

        Returns:
            list: List of sampled infohashes.
        """
        samples = self._session.dht_sample_infohashes(count)
        return samples

    def dht_state(self):
        """
        Retrieves the current state of the DHT.

        Returns:
            str: The state of the DHT.
        """
        state = self._session.dht_state()
        return state

    def download_rate_limit(self):
        """
        Retrieves the current download rate limit.

        Returns:
            int: Download rate limit in bytes per second.
        """
        return self._session.download_rate_limit()

    def find_torrent(self, info_hash):
        """
        Finds a torrent in the session by its info hash.

        Args:
            info_hash: The info hash of the torrent to find.

        Returns:
            lt.torrent_handle or None: The torrent handle if found, else None.
        """
        torrent_handle = self._session.find_torrent(info_hash)
        return torrent_handle

    def get_dht_settings(self):
        """
        Retrieves the current DHT settings.

        Returns:
            libtorrent.dht_settings: The DHT settings object.
        """
        settings = self._session.get_dht_settings()
        return settings

    def get_ip_filter(self):
        """
        Retrieves the current IP filter.

        Returns:
            libtorrent.ip_filter: The IP filter object.
        """
        ip_filter = self._session.get_ip_filter()
        return ip_filter

    def get_pe_settings(self):
        """
        Retrieves the peer-to-peer settings.

        Returns:
            libtorrent.pe_settings: The P2P settings object.
        """
        pe_settings = self._session.get_pe_settings()
        return pe_settings

    def get_peer_class(self, peer_class_id):
        """
        Retrieves a peer class by its ID.

        Args:
            peer_class_id (int): The ID of the peer class.

        Returns:
            libtorrent.peer_class: The peer class object.
        """
        peer_class = self._session.get_peer_class(peer_class_id)
        return peer_class

    def get_settings(self):
        """
        Retrieves the current session settings.

        Returns:
            libtorrent.settings_pack: The session settings object.
        """
        settings = self._session.get_settings()
        return settings

    def get_torrent_status(self, torrent_handle):
        """
        Retrieves the status of a specific torrent.

        Args:
            torrent_handle: The handle of the torrent.

        Returns:
            libtorrent.torrent_status: The torrent status object.
        """
        status = self._session.get_torrent_status(torrent_handle)
        return status

    def get_torrents(self):
        """
        Retrieves all torrents in the session.

        Returns:
            list: List of torrent handles.
        """
        torrents = self._session.get_torrents()
        return torrents

    def global_peer_class_id(self):
        """
        Retrieves the global peer class ID.

        Returns:
            int: The global peer class ID.
        """
        peer_class_id = self._session.global_peer_class_id()
        return peer_class_id

    def i2p_proxy(self, proxy):
        """
        Sets the I2P proxy for the session.

        Args:
            proxy: The I2P proxy to set.
        """
        self._session.i2p_proxy(proxy)
        return True  # Indicate success

    def id(self):
        """
        Retrieves the session's unique identifier.

        Returns:
            str: The session ID.
        """
        session_id = self._session.id()
        return session_id

    def is_dht_running(self):
        """
        Checks if the DHT is running.

        Returns:
            bool: True if DHT is running, else False.
        """
        return self._session.is_dht_running()

    def is_listening(self):
        """
        Checks if the session is listening for incoming connections.

        Returns:
            bool: True if listening, else False.
        """
        return self._session.is_listening()

    def is_paused(self):
        """
        Checks if the session is paused.

        Returns:
            bool: True if paused, else False.
        """
        return self._session.is_paused()

    def listen_on(self, port, num_ports=1):
        """
        Starts listening on the specified port.

        Args:
            port (int): The port number to listen on.
            num_ports (int): The number of ports to try.

        Returns:
            tuple: (port, status) where status indicates success or failure.
        """
        result = self._session.listen_on(port, num_ports)
        return result

    def listen_port(self):
        """
        Retrieves the port number the session is listening on.

        Returns:
            int: The listening port number.
        """
        port = self._session.listen_port()
        return port

    def load_state(self, state):
        """
        Loads a saved session state.

        Args:
            state: The state data to load.
        """
        self._session.load_state(state)
        return True  # Indicate success

    def local_download_rate_limit(self):
        """
        Retrieves the local download rate limit.

        Returns:
            int: Local download rate limit in bytes per second.
        """
        return self._session.local_download_rate_limit()

    def local_peer_class_id(self):
        """
        Retrieves the local peer class ID.

        Returns:
            int: The local peer class ID.
        """
        return self._session.local_peer_class_id()

    def local_upload_rate_limit(self):
        """
        Retrieves the local upload rate limit.

        Returns:
            int: Local upload rate limit in bytes per second.
        """
        return self._session.local_upload_rate_limit()

    def max_connections(self):
        """
        Retrieves the maximum number of connections allowed.

        Returns:
            int: Maximum number of connections.
        """
        return self._session.max_connections()

    def num_connections(self):
        """
        Retrieves the current number of active connections.

        Returns:
            int: Number of active connections.
        """
        return self._session.num_connections()

    def outgoing_ports(self):
        """
        Retrieves the range of outgoing ports.

        Returns:
            tuple: The range of outgoing ports (min, max).
        """
        ports = self._session.outgoing_ports()
        return ports

    def pause(self):
        """
        Pauses the session.
        """
        self._session.pause()
        return True  # Indicate success

    def peer_proxy(self, proxy):
        """
        Sets the peer proxy for the session.

        Args:
            proxy: The peer proxy to set.
        """
        self._session.peer_proxy(proxy)
        return True  # Indicate success

    def pop_alerts(self):
        """
        Pops alerts from the session's alert queue.

        Returns:
            list: List of alerts.
        """
        alerts = self._session.pop_alerts()
        return alerts

    def post_dht_stats(self):
        """
        Posts DHT statistics.

        Returns:
            libtorrent.dht_stats: DHT statistics object.
        """
        stats = self._session.post_dht_stats()
        return stats

    def post_session_stats(self):
        """
        Posts session statistics.

        Returns:
            libtorrent.session_stats: Session statistics object.
        """
        stats = self._session.post_session_stats()
        return stats

    def post_torrent_updates(self):
        """
        Posts torrent updates.

        Returns:
            libtorrent.torrent_updates: Torrent updates object.
        """
        updates = self._session.post_torrent_updates()
        return updates

    def set_proxy(self, proxy_type, proxy):
        """
        Sets the network proxy for the session.

        Args:
            proxy_type: The type of proxy (e.g., HTTP, SOCKS).
            proxy: The proxy address.
        """
        self._session.set_proxy(proxy_type, proxy)
        return True  # Indicate success

    def refresh_torrent_status(self, torrent_handle):
        """
        Refreshes the status of a specific torrent.

        Args:
            torrent_handle: The handle of the torrent.
        """
        self._session.refresh_torrent_status(torrent_handle)
        return True  # Indicate success

    def remove_torrent(self, torrent_handle, options=0):
        """
        Removes a torrent from the session.

        Args:
            torrent_handle: The handle of the torrent to remove.
            options (int): Removal options.

        Returns:
            bool: True if the torrent was removed, else False.
        """
        result = self._session.remove_torrent(torrent_handle, options)
        return result

    def reopen_map_ports(self):
        """
        Reopens the mapped ports.

        Returns:
            bool: True if ports were reopened successfully, else False.
        """
        result = self._session.reopen_map_ports()
        return result

    def reopen_network_sockets(self):
        """
        Reopens the network sockets.

        Returns:
            bool: True if network sockets were reopened successfully, else False.
        """
        result = self._session.reopen_network_sockets()
        return result

    def resume(self):
        """
        Resumes the session if it was paused.
        """
        self._session.resume()
        return True  # Indicate success

    def save_state(self):
        """
        Saves the current session state.

        Returns:
            bytes: The saved state data.
        """
        state = self._session.save_state()
        return state

    def set_alert_fd(self, fd):
        """
        Sets the file descriptor for alert notifications.

        Args:
            fd: The file descriptor to set.
        """
        self._session.set_alert_fd(fd)
        return True  # Indicate success

    def set_alert_mask(self, mask):
        """
        Sets the alert mask for the session.

        Args:
            mask: The alert mask to set.
        """
        self._session.set_alert_mask(mask)
        return True  # Indicate success

    def set_alert_notify(self, callback):
        """
        Sets the callback function for alert notifications.

        Args:
            callback: The callback function to set.
        """
        self._session.set_alert_notify(callback)
        return True  # Indicate success

    def set_alert_queue_size_limit(self, limit):
        """
        Sets the alert queue size limit.

        Args:
            limit (int): The maximum number of alerts to queue.
        """
        self._session.set_alert_queue_size_limit(limit)
        return True  # Indicate success

    def set_dht_proxy(self, proxy):
        """
        Sets the DHT proxy for the session.

        Args:
            proxy: The DHT proxy to set.
        """
        self._session.set_dht_proxy(proxy)
        return True  # Indicate success

    def set_dht_settings(self, settings):
        """
        Sets the DHT settings for the session.

        Args:
            settings: The DHT settings to apply.
        """
        self._session.set_dht_settings(settings)
        return True  # Indicate success

    def set_download_rate_limit(self, rate):
        """
        Sets the global download rate limit.

        Args:
            rate (int): Download rate limit in bytes per second.
        """
        self._session.set_download_rate_limit(rate)
        self._download_rate_limit = rate
        return self._download_rate_limit

    def set_i2p_proxy(self, proxy):
        """
        Sets the I2P proxy for the session.

        Args:
            proxy: The I2P proxy to set.
        """
        self._session.set_i2p_proxy(proxy)
        return True  # Indicate success

    def set_ip_filter(self, ip_filter):
        """
        Sets the IP filter for the session.

        Args:
            ip_filter: The IP filter to apply.
        """
        self._session.set_ip_filter(ip_filter)
        return True  # Indicate success

    def set_local_download_rate_limit(self, rate):
        """
        Sets the local download rate limit.

        Args:
            rate (int): Local download rate limit in bytes per second.
        """
        self._session.set_local_download_rate_limit(rate)
        return self._session.local_download_rate_limit()

    def set_local_upload_rate_limit(self, rate):
        """
        Sets the local upload rate limit.

        Args:
            rate (int): Local upload rate limit in bytes per second.
        """
        self._session.set_local_upload_rate_limit(rate)
        return self._session.local_upload_rate_limit()

    def set_max_connections(self, max_conn):
        """
        Sets the maximum number of connections allowed.

        Args:
            max_conn (int): Maximum number of connections.
        """
        self._session.set_max_connections(max_conn)
        return self._session.max_connections()

    def set_max_half_open_connections(self, max_half_open):
        """
        Sets the maximum number of half-open connections.

        Args:
            max_half_open (int): Maximum number of half-open connections.
        """
        self._session.set_max_half_open_connections(max_half_open)
        return self._session.max_half_open_connections()

    def set_max_uploads(self, max_uploads):
        """
        Sets the maximum number of simultaneous uploads.

        Args:
            max_uploads (int): Maximum number of uploads.
        """
        self._session.set_max_uploads(max_uploads)
        return self._session.max_uploads()

    def set_pe_settings(self, pe_settings):
        """
        Sets the peer-to-peer settings for the session.

        Args:
            pe_settings: The P2P settings to apply.
        """
        self._session.set_pe_settings(pe_settings)
        return self._session.get_pe_settings()

    def set_peer_class(self, peer_class_id, peer_class):
        """
        Sets a peer class with the given ID.

        Args:
            peer_class_id (int): The ID of the peer class.
            peer_class: The peer class to set.
        """
        self._session.set_peer_class(peer_class_id, peer_class)
        return self._session.get_peer_class(peer_class_id)

    def set_peer_class_filter(self, filter):
        """
        Sets the peer class filter.

        Args:
            filter: The filter to apply to peer classes.
        """
        self._session.set_peer_class_filter(filter)
        return self._session.get_peer_class_filter()

    def set_peer_class_type_filter(self, type_filter):
        """
        Sets the peer class type filter.

        Args:
            type_filter: The type filter to apply.
        """
        self._session.set_peer_class_type_filter(type_filter)
        return self._session.get_peer_class_type_filter()

    def set_peer_id(self, peer_id):
        """
        Sets the peer ID for the session.

        Args:
            peer_id (bytes): The peer ID to set.
        """
        self._session.set_peer_id(peer_id)
        return self._session.get_peer_id()

    def set_peer_proxy(self, proxy):
        """
        Sets the peer proxy for the session.

        Args:
            proxy: The peer proxy to set.
        """
        self._session.set_peer_proxy(proxy)
        return True  # Indicate success

    def set_tracker_proxy(self, proxy):
        """
        Sets the tracker proxy for the session.

        Args:
            proxy: The tracker proxy to set.
        """
        self._session.set_tracker_proxy(proxy)
        return True  # Indicate success

    def set_upload_rate_limit(self, rate):
        """
        Sets the global upload rate limit.

        Args:
            rate (int): Upload rate limit in bytes per second.
        """
        self._session.set_upload_rate_limit(rate)
        self._upload_rate_limit = rate
        return self._upload_rate_limit

    def set_web_seed_proxy(self, proxy):
        """
        Sets the web seed proxy for the session.

        Args:
            proxy: The web seed proxy to set.
        """
        self._session.set_web_seed_proxy(proxy)
        return True  # Indicate success

    def ssl_listen_port(self):
        """
        Retrieves the SSL listening port.

        Returns:
            int: SSL listening port number.
        """
        port = self._session.ssl_listen_port()
        return port

    def start_dht(self):
        """
        Starts the DHT in the session.
        """
        self._session.start_dht()
        return True  # Indicate success

    def start_lsd(self):
        """
        Starts Local Service Discovery (LSD) in the session.
        """
        self._session.start_lsd()
        return True  # Indicate success

    def start_natpmp(self):
        """
        Starts NAT-PMP in the session.
        """
        self._session.start_natpmp()
        return True  # Indicate success

    def start_upnp(self):
        """
        Starts UPnP in the session.
        """
        self._session.start_upnp()
        return True  # Indicate success

    def status(self):
        """
        Retrieves the current session status.

        Returns:
            libtorrent.session_status: Session status object.
        """
        status = self._session.status()
        return status

    def stop_dht(self):
        """
        Stops the DHT in the session.
        """
        self._session.stop_dht()
        return True  # Indicate success

    def stop_lsd(self):
        """
        Stops Local Service Discovery (LSD) in the session.
        """
        self._session.stop_lsd()
        return True  # Indicate success

    def stop_natpmp(self):
        """
        Stops NAT-PMP in the session.
        """
        self._session.stop_natpmp()
        return True  # Indicate success

    def stop_upnp(self):
        """
        Stops UPnP in the session.
        """
        self._session.stop_upnp()
        return True  # Indicate success

    def tcp(self):
        """
        Retrieves TCP-related information.

        Returns:
            libtorrent.tcp_settings: TCP settings object.
        """
        tcp_info = self._session.tcp()
        return tcp_info

    def tcp_peer_class_id(self):
        """
        Retrieves the TCP peer class ID.

        Returns:
            int: TCP peer class ID.
        """
        peer_class_id = self._session.tcp_peer_class_id()
        return peer_class_id

    def tracker_proxy(self):
        """
        Retrieves the tracker proxy.

        Returns:
            libtorrent.proxy_settings: The tracker proxy object.
        """
        proxy = self._session.tracker_proxy()
        return proxy

    def udp(self):
        """
        Retrieves UDP-related information.

        Returns:
            libtorrent.udp_settings: UDP settings object.
        """
        udp_info = self._session.udp()
        return udp_info

    def upload_rate_limit(self):
        """
        Retrieves the current upload rate limit.

        Returns:
            int: Upload rate limit in bytes per second.
        """
        return self._session.upload_rate_limit()

    def wait_for_alert(self, timeout):
        """
        Waits for an alert within the specified timeout.

        Args:
            timeout (float): Timeout in seconds.

        Returns:
            libtorrent.alert: The alert if received within the timeout, else None.
        """
        alert = self._session.wait_for_alert(timeout)
        return alert

    def web_seed_proxy(self):
        """
        Retrieves the web seed proxy.

        Returns:
            libtorrent.proxy_settings: The web seed proxy object.
        """
        proxy = self._session.web_seed_proxy()
        return proxy
