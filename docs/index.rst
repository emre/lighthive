
lighthive
=================================

lighthive is a **light** python client to interact with the HIVE blockchain.
It's simple and stupid. It doesn't interfere the process between the developer
and the HIVE node.

.. figure::  https://i.imgur.com/ivmjHkv.png
   :width: 600

Features
----------
- No hard-coded methods. All potential future appbase methods are automatically supported.
- Retry and Failover support for node errors and timeouts. See :doc:`/retryandfailover`.


Limitations
------------
- No support for pre-appbase nodes.
- No magic methods and encapsulation over well-known blockchain objects. (Comment, Post, Account, etc.)

Installation
-------------

lighthive requires python3.6 and above. Even though it's easy to make it compatible
with lower versions, it's doesn't have support by design to keep the library simple.

You can install the library by typing to your console:

.. code-block:: bash

    $ (sudo) pip install lighthive

After that, you can continue with  :doc:`/gettingstarted`.

Documentation Pages
-----------

.. toctree::
   :maxdepth: 3

   gettingstarted
   retryandfailover
   broadcasting
   batch_rpc_calls
   helpers