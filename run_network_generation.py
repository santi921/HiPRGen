import sys
from reaction_filter import *
import pickle
from mpi4py import MPI

if len(sys.argv) != 5:
    print("python run_network_generation.py mol_entries_pickle_location bucket_db_location rn_db_location generation_report_location")

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

mol_entries_pickle_file = sys.argv[1]
bucket_db_file = sys.argv[2]
rn_db_file = sys.argv[3]
report_file = sys.argv[4]

with open(mol_entries_pickle_file, 'rb') as f:
    mol_entries = pickle.load(f)


if rank == DISPATCHER_RANK:
    dispatcher(bucket_db_file)
elif rank == NETWORK_WRITER_RANK:
    reaction_network_writer(rn_db_file)
elif rank == LOGGING_WRITER_RANK:
    reaction_logging_writer(mol_entries, report_file)
else:
    reaction_filter(mol_entries, bucket_db_file)