END=$1
CURRENT_RUN=0

call_db()
{
    echo "process $i start ....."
    python3.6 testDB.py
    echo "...... process $i done"
}

for i in $(seq 1 $END)
do
    CURRENT_RUN=$i
    call_db $i &
done
