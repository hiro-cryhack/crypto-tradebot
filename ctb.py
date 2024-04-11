from web3 import Web3
import random
import time

# 以太坊节点的 RPC 地址
rpc_url = "http://localhost:8545"  # 替换成你的以太坊节点的 RPC 地址

# 你的私钥
private_key = "YOUR_PRIVATE_KEY_HERE"  # 替换成你的以太坊钱包的私钥

# 以太坊账户地址
account_address = "YOUR_ACCOUNT_ADDRESS_HERE"  # 替换成你的以太坊钱包的地址

# 连接到以太坊节点
web3 = Web3(Web3.HTTPProvider(rpc_url))

# 获取以太坊账户的nonce值
def get_nonce():
    return web3.eth.getTransactionCount(account_address)

# 发送以太币的方法
def send_transaction(to, value, nonce):
    transaction = {
        'to': to,
        'value': web3.toWei(value, 'ether'),
        'gas': 2000000,  # 设置gas上限
        'gasPrice': web3.toWei('50', 'gwei'),  # 设置gas价格
        'nonce': nonce,
        'chainId': 1,
    }
    signed_txn = web3.eth.account.signTransaction(transaction, private_key)
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return txn_hash.hex()

# 部署简易合约的方法
def deploy_contract(nonce):
    contract_code = "0x606060405260405161023e38038061023e8339810160405280510160008054600160a060020a0319163317905561019c806100506000396000f3606060405260e060020a6000350463a9059cbb8114610043578063d0973e4e14610064575b005b61009e60048080359060200190919050506100e0565b6040518082815260200191505060405180910390f35b600060006000600060005054906101000a900460ff16905090565b60006000600060006101000a81548160ff021916908360ff1602179055505b50565b5600a165627a7a72305820f9b012b1898b99577ab85d66cdab09f4784ff0dcf82da0c80e37fb8577ab84e80029"
    
    transaction = {
        'data': contract_code,
        'gas': 2000000,  # 设置gas上限
        'gasPrice': web3.toWei('50', 'gwei'),  # 设置gas价格
        'nonce': nonce,
        'chainId': 1,
    }
    signed_txn = web3.eth.account.signTransaction(transaction, private_key)
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return txn_hash.hex()

# 主程序
def main():
    while True:
        # 随机生成转账金额
        to = "0xrecipientaddress"  # 替换成接收地址
        value = random.random() * 0.01
        
        # 获取nonce值
        nonce = get_nonce()
        
        # 调用发送以太币方法
        tx_hash = send_transaction(to, value, nonce)
        print(f"Transferred {value} ETH to {to}. Tx Hash: {tx_hash}")
        
        # 调用部署简易合约方法
        contract_hash = deploy_contract(nonce + 1)  # 使用不同的nonce来部署合约
        print(f"Deployed simple contract. Tx Hash: {contract_hash}")
        
        # 延迟执行
        time.sleep(random.random() * 3)

if __name__ == "__main__":
    main()
