<template>
  <div class="landing">
    <h1>Welcome to the Dashboard</h1>
    <button @click="navigate('recordEditor')">Go to Record Editor</button>
    <button @click="navigate('binaryEditor')">Go to Binary Affirmations Editor</button>
    <input v-model="channelId" placeholder="Enter channel ID" />
    <button @click="saveChannel">Save Channel</button>
    <div id="cy" class="cytoscape-container"></div>
  </div>
</template>

<script>
import cytoscape from 'cytoscape';
import axios from 'axios';

export default {
  name: 'LandingPage',
  data() {
    return {
      channelId: '',
      chart: null,
      datacollection: {
        labels: [],
        datasets: [{
          label: 'Relations',
          data: [],
          borderColor: "#3e95cd",
          fill: false
        }]
      }
    };
  },
  async mounted() {
    try {
      const relationResponse = await axios.get('http://localhost:3001/relations/');
      const relations = relationResponse.data;
      const channelResponse = await axios.get('http://localhost:3001/channels/');
      const channels = channelResponse.data;

      // Convert channels to a map for easy lookup
      const channelMap = channels.reduce((acc, channel) => {
        acc[channel.channelId] = channel; // Adjusted to use channelId
        return acc;
      }, {});

      var elements = [];
      relations.forEach(relation => {
        const channelA = channelMap[relation.channel_a];
        const channelB = channelMap[relation.channel_b];
        // Add 2 nodes and un edge
        elements.push({ data: { id: channelA.channelId, average_score: channelA.average_score } });  // Adjusted to use channelId
        elements.push({ data: { id: channelB.channelId, average_score: channelB.average_score } });
        elements.push({
          data: {
            id: relation.channel_a + '-' + relation.channel_b,
            source: relation.channel_a,
            target: relation.channel_b,
            relation: relation.relation 
          }
        });
      });

      cytoscape({
          container: document.getElementById('cy'),
          elements: elements,
          style: [
          {
            selector: 'node',
            style: {
              label: function( ele ){
                return ele.data('id') + ' : ' + ele.data('average_score');
              },
              'font-size': '5px',
            }
          },
          {
            selector: 'edge',
            style: {
              'curve-style': 'bezier',
              'width': 'data(relation)',     // set the edge width based on the relation value
              'label': 'data(relation)',     // display the relation value as a label on the edge
              'text-rotation': 'autorotate', // rotates the text so it's aligned with the edge
              'text-margin-y': -10,          // The offsets the text a bit from the edge
              'font-size': '8px'
            }
          }
        ],
          layout: {
            name: 'cose', // a force-directed layout
          }
        });
      // Initialize Cytoscape with modified elements
      // (The initialization code remains the same as before)
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  },
  methods: {
    navigate(route) {
      this.$emit('changeRoute', route);
    },
    async saveChannel() {
      try {
        const response = await axios.post('http://localhost:3001/saveChannel/', {
          channelId: this.channelId
        });
        
        if(response.data.success) {
          alert('Channel saved successfully!');
          this.channelId = '';
        } else {
          alert('Error saving channel');
        }
      } catch (error) {
        alert('Error saving channel');
      }
    },
    createChart() {
      const ctx = this.$refs.canvas.getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'line',
        data: this.datacollection,
        options: { responsive: true, maintainAspectRatio: false }
      });
    }
  }
};
</script>

<style scoped>
.landing {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}
.chart {
  width: 80%;
  height: 400px;
  margin-top: 20px;
}
</style>

<style scoped>
.cytoscape-container {
  width: 80%;
  height: 400px;
  margin-top: 20px;
  border: 1px solid #aaa;
}
</style>
