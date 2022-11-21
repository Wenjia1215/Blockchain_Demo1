#   Wenjia blockchain demo 1


from Block import Block


def runBlockchian():
    blockchain = []
    genesis_block = Block('The Times 03/Jan/2009 Chancellor on brink of second bailout for banks',
                          ['Wenjia sent 10 BTC to Sadjadi',
                           'Alex sent 2 BTC to Wenjia'])
    second_block = Block(genesis_block.block_hash, ['Wenjia sent 10 BTC to Sadjadi',
                                                    'Boss sent 2 BTC to Wenjia'])
    third_block = Block(second_block.block_hash, ['Sadjadi received 100 BTC from Wen',
                                                  'Wen got block reward'])

    print('Genesis block hash\n', genesis_block.block_hash)
    print('second block hash\n', second_block.block_hash)
    print('third block hash\n', third_block.block_hash)


if __name__ == '__main__':
    runBlockchian()

    '''
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

    '''