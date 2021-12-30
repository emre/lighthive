
Getting Started
=================================

Client class is the primary class you will work with.


.. code-block:: python

    from lighthive.client import Client

    client = Client()


Appbase nodes support different `api namespaces <https://developers.hive.io/apidefinitions/#apidefinitions-condenser-api>`_.

Client class uses **condenser_api** as default. Follow the official developer portal's `api definitions <https://developers.hive.io/apidefinitions/>`_
to explore available methods.

Automatic Node Selection
""""""""

If you prefer, you can pass ``automatic_node_selection`` flag True to the ``Client``. 

That way, lighthive requests a ``get_dynamic_global_properties`` call to the each defined node, and sorts nodes by their response time.

.. code-block:: bash

    2021-12-30 17:20:28,515 lighthive    INFO     Measurements:
    https://rpc.ausbit.dev: 0.12 [s]
    https://api.openhive.network: 0.12 [s]
    https://hive-api.arcange.eu: 0.12 [s]
    https://hived.emre.sh: 0.14 [s]
    https://api.deathwing.me: 0.15 [s]
    https://rpc.ecency.com: 0.16 [s]
    https://api.hive.blue: 0.19 [s]
    https://api.pharesim.me: 0.28 [s]
    https://api.hive.blog: 0.46 [s]
    https://techcoderx.com: 0.77 [s]

    2021-12-30 17:20:28,516 lighthive    INFO     Automatic node selection took  0.81 seconds.
    2021-12-30 17:20:28,516 lighthive    INFO     Node set as https://rpc.ausbit.dev


Since it's a time-consuming operation, this is an optional flag, and it's default is False.


Examples
""""""""

**Get Dynamic Global Properties**

.. code-block:: python

    props = client.get_dynamic_global_properties()

    print(props)

**Get Current Reserve Ratio**

.. code-block:: python

    ratio = c('witness_api').get_reserve_ratio()

    print(ratio)


**Get @emrebeyler's account history**

.. code-block:: python

    history = c.get_account_history("emrebeyler", 1000, 10)

    for op in history:
        print(op)

**Get top 100 witness list**

.. code-block:: python

    witness_list = client.get_witnesses_by_vote(None, 100)

    print(witness_list)


It's the same convention for every api type and every call on appbase nodes.

.. important ::
    Since, api_type is set when the client instance is called, it is not thread-safe to share Client instances between threads.


Optional parameters of Client
"""""""""

Even though, you don't need to pass any parameters to the ``Client``, you have some options
to choose.


.. function:: __init__(self, nodes=None, keys=None, connect_timeout=3,
                 read_timeout=30, loglevel=logging.ERROR, chain=None)

   :param nodes: A list of appbase nodes. (Defaults:  "https://api.hive.blog", "https://api.hivekings.com",
 "https://anyx.io")
   :param keys: A list of private keys.
   :param connect_timeout: Integer. Connect timeout for nodes. (Default:3 seconds.)
   :param read_timeout: Integer. Read timeout for nodes. (Default: 30 seconds.)
   :param loglevel: Integer. (Ex: logging.DEBUG)
   :param chain: String. The blockhain we're working with. (Default: HIVE)
   :param automatic_node_selection: Bool. True/False (Default: False)


See :doc:`/broadcasting` to find out how to broadcast transactions into the blockchain.