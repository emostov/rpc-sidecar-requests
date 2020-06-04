from reconcile import *

def main():
	block_number = int(get_latest_block_number(sidecar_url))
	for i in range(0, block_number):
		block_data = get_block(sidecar_url, block)
		if block_data and address in block_data:
				print(block_data)



main()
