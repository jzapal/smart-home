<template>
  <div v-if="fetching">
    Loading...
  </div>
  <div v-else-if="error">
    Oh no... {{error}}
  </div>
  <div v-else>
    <ul v-if="data">
      <div class="card" v-for="sensor in sensors">
        <div class="card-title">{{ sensor.name }}</div>
        <div class="card-body">
        </div>
      </div>
    </ul>
  </div>
</template>

<script>
import { useQuery } from '@urql/vue';

export default {
  setup() {
    const result = useQuery({
      query: `
        {
          sensors {
            id
            name
          }
        }
      `
    });

    return {
      fetching: result.fetching,
      data: result.data,
      error: result.error,
    };
  }
};
</script>